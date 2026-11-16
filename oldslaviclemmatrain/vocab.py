import json


class Vocab:
    def __init__(self, sep_char="⟂"):
        self.sep_char = sep_char
        self.char2idx = {"<pad>": 0, "<sos>": 1, "<eos>": 2, "<unk>": 3}
        self.idx2char = {i: c for c, i in self.char2idx.items()}

    def build(self, examples):
        for ch in [" ", self.sep_char]:
            if ch not in self.char2idx:
                idx = len(self.char2idx)
                self.char2idx[ch] = idx
                self.idx2char[idx] = ch
        for _, lemma, src_string in examples:
            for ch in src_string + lemma:
                if ch not in self.char2idx:
                    idx = len(self.char2idx)
                    self.char2idx[ch] = idx
                    self.idx2char[idx] = ch

    def encode(self, s):
        unk = self.char2idx["<unk>"]
        return [self.char2idx.get(ch, unk) for ch in s]

    def decode(self, ids):
        out = []
        for i in ids:
            if i == self.char2idx["<eos>"]:
                break
            if i > self.char2idx["<eos>"]:
                out.append(self.idx2char[i])
        return "".join(out)

    def to_dict(self):
        return {
            "char2idx": self.char2idx,
            "idx2char": {str(k): v for k, v in self.idx2char.items()},
            
        }

    def save(self, path):
        with open(path, "w", encoding="utf8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
