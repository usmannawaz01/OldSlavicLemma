# OldSlavicLemma

**OldSlavicLemma** is a neural sequence-to-sequence lemmatizer for Early Slavic languages, with a focus on **Old Church Slavonic (OCS)** and **Old East Slavic (OES)**. The model is designed for historical and medieval Slavic texts with rich morphology, orthographic variation, and limited annotated resources.



## Online demos

Two Hugging Face Spaces are available.

### 1. OldSlavicLemma interactive interface

Use this demo to lemmatize individual words/ Tokens or text interactively:

https://usmannawaz01.github.io/OldSlavicLemma/

### 2. CoNLL-U comparison and reproducibility interface

Use this demo for CoNLL-U based comparison and reproducibility without retraining:

https://huggingface.co/spaces/usmannawaz/oldslaviclemma-conllu

## Supported languages and treebanks

The main experiments focus on Early Slavic Universal Dependencies treebanks:

- Old Church Slavonic — PROIEL
- Old East Slavic — Birchbark
- Old East Slavic — RNC
- Old East Slavic — TOROT


The model is also evaluated on additional historical and modern Universal Dependencies treebanks.


## Evaluation settings

The paper reports two main evaluation settings.

### Gold-tokenization setting

In this setting, the official UD tokenization and sentence boundaries are preserved. The model predicts lemmas for already tokenized input.

Metric:

- Token-level lemma exact-match accuracy

### Raw-text setting

In this setting, systems are evaluated from raw input text to CoNLL-U output using the official CoNLL-2018 evaluation script.

Metric:

- Lemmas F1 score from the CoNLL-2018 evaluation script


## Repository status

This repository will contain the source code, evaluation scripts, model configuration files, and instructions for reproducing the experiments reported in the paper.
