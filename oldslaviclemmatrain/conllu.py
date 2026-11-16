import re


def parse_conllu_sentences(path):
    text = open(path, encoding="utf8").read().strip()
    sents = []
    for block in re.split(r"\n\n+", text):
        sent = []
        for line in block.split("\n"):
            if not line or line.startswith("#"):
                continue
            cols = line.split("\t")
            if len(cols) != 10 or "-" in cols[0] or "." in cols[0]:
                continue
            sent.append((cols[1], cols[2]))
        if sent:
            sents.append(sent)
    return sents
