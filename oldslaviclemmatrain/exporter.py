import json
import os
import torch


def clean_name(name):
    return "".join(ch for ch in str(name) if ch.isalnum()).lower()


def write_export(save_dir, model, vocab, settings, model_name=None):
    os.makedirs(save_dir, exist_ok=True)
    if not model_name:
        model_name = settings.model_id
    model_file = f"{clean_name(model_name)}model.pt"

    torch.save(model.state_dict(), os.path.join(save_dir, model_file))
    vocab.save(os.path.join(save_dir, "vocab.json"))

    config = {
        "model_id": settings.model_id,
        "char_emb_dim": settings.char_emb_dim,
        "hidden_size": settings.hidden_size,
        "drop_prob": settings.drop_prob,
        "num_heads": settings.num_heads,
        "max_gen_len": settings.max_gen_len,
        "k_context": settings.k_context,
        "sep_char": settings.sep_char,
        "model_type": "char_lstm_attention_lemmatizer",
        "vocab_size": len(vocab.char2idx)
    }

    with open(os.path.join(save_dir, "config.json"), "w", encoding="utf8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    registry = {
        "id": settings.model_id,
        "folder": os.path.basename(os.path.normpath(save_dir)),
        "model_file": model_file,
        "vocab_file": "vocab.json",
        "config_file": "config.json",
        "model_type": "char_lstm_attention_lemmatizer",
        "vocab_size": len(vocab.char2idx)
    }

    with open(os.path.join(save_dir, "registryentry.json"), "w", encoding="utf8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)

    return model_file
