import os
from dataclasses import dataclass
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torch.optim.lr_scheduler import ReduceLROnPlateau
from tqdm import tqdm
from lion_pytorch import Lion

from .conllu import parse_conllu_sentences
from .examples import make_context_examples
from .vocab import Vocab
from .dataset import LemmaDataset
from .architecture import LemmaModel
from .exporter import write_export


@dataclass
class TrainSettings:
    train_conllu: str
    dev_conllu: str
    test_conllu: str
    save_dir: str
    model_id: str = "model"
    batch_size: int = 32
    epochs: int = 75
    lr: float = 1.5e-4
    weight_decay: float = 3e-5
    char_emb_dim: int = 96
    hidden_size: int = 128
    drop_prob: float = 0.30
    clip_norm: float = 5.0
    num_heads: int = 16
    max_gen_len: int = 30
    early_stop_patience: int = 15
    k_context: int = 2
    sep_char: str = "⟂"


def evaluate(model, loader, vocab):
    model.eval()
    total, correct = 0, 0
    with torch.no_grad():
        for forms, golds, src, tgt, src_lens in tqdm(loader, desc="Eval"):
            preds = model.generate(src, src_lens, vocab)
            for p, g in zip(preds, golds):
                correct += int(p == g)
                total += 1
    return correct / total if total > 0 else 0.0





def train_model(settings):
    os.makedirs(settings.save_dir, exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}\n")

    train_s = parse_conllu_sentences(settings.train_conllu)
    dev_s = parse_conllu_sentences(settings.dev_conllu)
    test_s = parse_conllu_sentences(settings.test_conllu)

    train_ex = make_context_examples(train_s, k=settings.k_context, sep_char=settings.sep_char)
    dev_ex = make_context_examples(dev_s, k=settings.k_context, sep_char=settings.sep_char)
    test_ex = make_context_examples(test_s, k=settings.k_context, sep_char=settings.sep_char)

    vocab = Vocab(sep_char=settings.sep_char)
    vocab.build(train_ex)

    train_ds = LemmaDataset(train_ex, vocab, device)
    dev_ds = LemmaDataset(dev_ex, vocab, device)
    test_ds = LemmaDataset(test_ex, vocab, device)

    tr_loader = DataLoader(train_ds, settings.batch_size, shuffle=True, collate_fn=train_ds.collate_fn)
    dv_loader = DataLoader(dev_ds, settings.batch_size, shuffle=False, collate_fn=dev_ds.collate_fn)
    te_loader = DataLoader(test_ds, settings.batch_size, shuffle=False, collate_fn=test_ds.collate_fn)

    model = LemmaModel(
        len(vocab.char2idx),
        char_emb_dim=settings.char_emb_dim,
        hidden_size=settings.hidden_size,
        drop_prob=settings.drop_prob,
        num_heads=settings.num_heads,
        max_gen_len=settings.max_gen_len
    ).to(device)

    optimizer = Lion(model.parameters(), lr=settings.lr, weight_decay=settings.weight_decay)
    scheduler = ReduceLROnPlateau(optimizer, mode="max", factor=0.5, patience=3, min_lr=1e-6)

    

    best_em = 0.0
    train_losses, val_losses, dev_ems = [], [], []
    pad_id = vocab.char2idx["<pad>"]
    epochs_no_improve = 0

    for ep in range(1, settings.epochs + 1):
        model.train()
        train_loss_sum, train_tok_sum = 0.0, 0

        for _, _, src, tgt, src_lens in tqdm(tr_loader, desc=f"Train {ep}/{settings.epochs}"):
            optimizer.zero_grad()
            logits = model(src, src_lens, tgt)
            vocab_size = logits.size(-1)

            n_tokens = (tgt[:, 1:] != pad_id).sum().clamp_min(1)
            loss_sum = F.cross_entropy(
                logits.view(-1, vocab_size),
                tgt[:, 1:].reshape(-1),
                ignore_index=pad_id,
                reduction="sum"
            )
            loss = loss_sum / n_tokens
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), settings.clip_norm)
            optimizer.step()

            train_loss_sum += loss_sum.item()
            train_tok_sum += int(n_tokens.item())

        train_losses.append(train_loss_sum / max(1, train_tok_sum))

        model.eval()
        val_sum, val_tok = 0.0, 0
        with torch.no_grad():
            for _, _, src_v, tgt_v, sl_v in dv_loader:
                out_v = model(src_v, sl_v, tgt_v)
                vocab_size_v = out_v.size(-1)
                lv_sum = F.cross_entropy(
                    out_v.view(-1, vocab_size_v),
                    tgt_v[:, 1:].reshape(-1),
                    ignore_index=pad_id,
                    reduction="sum"
                )
                n_tok = (tgt_v[:, 1:] != pad_id).sum().item()
                val_sum += lv_sum.item()
                val_tok += n_tok

        val_losses.append(val_sum / max(1, val_tok))

        dev_em = evaluate(model, dv_loader, vocab)
        dev_ems.append(dev_em)

        print(f"Epoch {ep}: train_loss={train_losses[-1]:.4f}, val_loss={val_losses[-1]:.4f}, EM={dev_em:.2%}")
        scheduler.step(dev_em)

        if dev_em > best_em:
            best_em = dev_em
            torch.save(model.state_dict(), os.path.join(settings.save_dir, "best.pt"))
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1

        if epochs_no_improve >= settings.early_stop_patience:
            print(f"Early stopping triggered at epoch {ep} (no improvement for {settings.early_stop_patience} epochs).")
            break

        
        
            
            
            
            
                
           

    print(f"\n>>> Best dev EM = {best_em:.2%}")
    state = torch.load(os.path.join(settings.save_dir, "best.pt"), map_location=device)
    model.load_state_dict(state)
    final_test_em = evaluate(model, te_loader, vocab)
    print(f">>> Final test EM = {final_test_em:.2%}\n")

    
    model_file = write_export(settings.save_dir, model, vocab, settings, settings.model_id)

    best_path = os.path.join(settings.save_dir, "best.pt")
    if os.path.exists(best_path):
          os.remove(best_path)

    print(f"Saved exported model to: {os.path.join(settings.save_dir, model_file)}")






    print(f"Saved vocab to: {os.path.join(settings.save_dir, 'vocab.json')}")
    print(f"Saved config to: {os.path.join(settings.save_dir, 'config.json')}")
    print(f"Saved registry entry to: {os.path.join(settings.save_dir, 'registryentry.json')}")

    return {
        "best_dev_em": best_em,
        "final_test_em": final_test_em,
        "save_dir": settings.save_dir
    }
