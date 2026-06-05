def make_context_examples(sents, k=5, sep_char="⟂", repeat_form=1):
    ex = []
    for sent in sents:
        tokens = [w for w, _ in sent]
        for i, (form_i, lemma_i) in enumerate(sent):
            prev_tokens = tokens[max(0, i - k):i]
            next_tokens = tokens[i + 1:i + 1 + k]
            left = (" ".join(prev_tokens)).strip()
            right = (" ".join(next_tokens)).strip()
            src_left = (left + " ") if left else ""
            src_right = (" " + right) if right else ""
            center = form_i
            src_string = f"{src_left}{sep_char}{center}{sep_char}{src_right}"
            ex.append((form_i, lemma_i, src_string))
    return ex
