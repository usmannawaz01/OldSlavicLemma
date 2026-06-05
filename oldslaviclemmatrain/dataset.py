import torch
from torch.utils.data import Dataset


class LemmaDataset(Dataset):
    def __init__(self, examples, vocab, device):
        self.vocab = vocab
        self.device = device
        self.data = []
        for form, lemma, src_string in examples:
            src = [vocab.char2idx["<sos>"]] + vocab.encode(src_string) + [vocab.char2idx["<eos>"]]
            tgt = [vocab.char2idx["<sos>"]] + vocab.encode(lemma) + [vocab.char2idx["<eos>"]]
            self.data.append((form, lemma, src, tgt))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

    def collate_fn(self, batch):
        forms, lemmas, srcs, tgts = zip(*batch)
        src_lens = [len(s) for s in srcs]
        tgt_lens = [len(t) for t in tgts]
        max_src, max_tgt = max(src_lens), max(tgt_lens)
        pad_id = self.vocab.char2idx["<pad>"]

        def pad_to(seqs, max_len, pad_val):
            return [s + [pad_val] * (max_len - len(s)) for s in seqs]

        src_tensor = torch.tensor(pad_to(srcs, max_src, pad_id), device=self.device, dtype=torch.long)
        tgt_tensor = torch.tensor(pad_to(tgts, max_tgt, pad_id), device=self.device, dtype=torch.long)
        return forms, lemmas, src_tensor, tgt_tensor, torch.tensor(src_lens, device=self.device)
