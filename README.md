# OldSlavicLemma

**OldSlavicLemma** is a neural sequence-to-sequence lemmatizer for historical and low-resource languages, with a primary focus on **Old Church Slavonic (OCS)** and **Old East Slavic (OES)**.

The model is designed for texts with rich inflectional morphology, orthographic variation, and limited annotated resources. It uses a dictionary-free character-level encoder-decoder architecture with recurrent layers and attention mechanisms.

## Tags

`lemmatization` · `historical-nlp` · `old-church-slavonic` · `old-east-slavic` · `early-slavic` · `universal-dependencies` · `sequence-to-sequence` · `character-level-modeling` · `low-resource-nlp` · `morphology` · `pytorch`

## Project properties

- **Task:** Lemmatization
- **Model type:** Neural sequence-to-sequence lemmatizer
- **Input:** Token, word, or short text
- **Output:** Predicted lemma
- **Primary languages:** Old Church Slavonic and Old East Slavic
- **Primary treebanks:** PROIEL, Birchbark, RNC, TOROT
- **Additional evaluation:** 64 languages and 115 Universal Dependencies treebanks
- **Framework:** PyTorch
- **License:** CC BY-NC 4.0

## Online demo

Two online interfaces are available.

### 1. Interactive lemmatization demo

Use this demo to lemmatize individual words, tokens, or short text interactively:

https://usmannawaz01.github.io/OldSlavicLemma/

### 2. Pretrained models

Pretrained OldSlavicLemma models are available on Hugging Face:

https://huggingface.co/usmannawaz/oldslaviclemma

These resources are intended for reuse of the released models without retraining.

## Supported languages and treebanks

OldSlavicLemma is specialized for Early Slavic lemmatization, especially:

- Old Church Slavonic — PROIEL
- Old East Slavic — Birchbark
- Old East Slavic — RNC
- Old East Slavic — TOROT


In addition to Early Slavic, the model was evaluated on **64 languages** and **115 Universal Dependencies treebanks**. These experiments include both historical and contemporary languages and are intended to assess portability beyond the main Early Slavic setting.

## Evaluation settings

We reports two main evaluation settings.

### Gold-tokenization setting

Official UD tokenization and sentence boundaries are preserved. The model predicts lemmas for already-tokenized input.

**Metric**

- Accuracy

### Raw-tokenization setting

Raw input is first tokenized using an external tokenizer, and OldSlavicLemma is then used for lemma prediction.

**Metric**

- Lemmas F1 score from the official CoNLL-2018 evaluation script

## Repository status

This repository contains, or will contain, the resources required to reproduce the experiments:

- Source code for OldSlavicLemma
- Training and evaluation scripts
- Model configuration files
- CoNLL-U evaluation pipeline
- Instructions for reproducing UD v2.12 and UD v2.15 experiments
- Links to released pretrained models

## Citation

If you use OldSlavicLemma in your research, please cite:

```bibtex
@article{nawaz2025oldslaviclemma,
  title   = {OldSlavicLemma: A Neural Sequence-to-Sequence Model for Lemmatization of Early Slavic Languages},
  author  = {Nawaz, Usman and Lo Presti, Liliana and La Cascia, Marco},
  journal = {Natural Language Processing},
  year    = {2025}
}
