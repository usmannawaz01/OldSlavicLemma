# OldSlavicLemma

**OldSlavicLemma** is a neural sequence-to-sequence lemmatizer for historical and low-resource languages, with a primary focus on **Old Church Slavonic (OCS)** and **Old East Slavic (OES)**.

The model is designed for texts with rich inflectional morphology, orthographic variation, and limited annotated resources. It uses a dictionary-free character-level encoder-decoder architecture with recurrent layers and attention mechanisms.

## Tags

`lemmatization` · `historical-nlp` · `old-church-slavonic` · `old-east-slavic` · `early-slavic` · `universal-dependencies` · `sequence-to-sequence` · `character-level-modeling` · `low-resource-nlp` · `morphology` · `pytorch`


**Current status:** Pretrained models are available on Hugging Face, while the online demo, inference code, retraining code have not been released yet and planned for September.

## Online demo
An interactive demo is available here:
https://usmannawaz01.github.io/OldSlavicLemma/

The demo can be used to lemmatize individual words/tokens, or text.


## Pretrained models

Pretrained OldSlavicLemma models are available on Hugging Face:

https://huggingface.co/usmannawaz/oldslaviclemma

Use the Hugging Face repository if you want to download and reuse pretrained models without retraining.

## Project properties

- **Task:** Lemmatization
- **Model type:** Neural sequence-to-sequence lemmatizer
- **Input:** Text
- **Output:** Predicted lemma
- **Primary languages:** Old Church Slavonic and Old East Slavic
- **Primary treebanks:** PROIEL, Birchbark, RNC, TOROT
- **Framework:** PyTorch
- **Code license:** MIT License
- **Model weights license:** CC BY-NC 4.0



## Supported languages and treebanks

OldSlavicLemma is specialized for Early Slavic lemmatization, especially:

- Old Church Slavonic — PROIEL
- Old East Slavic — Birchbark
- Old East Slavic — RNC
- Old East Slavic — TOROT

The model was also evaluated on additional Universal Dependencies treebanks to test portability beyond the main Early Slavic setting.


Language,Treebank,Oldslaviclemma
"Afrikaans","AfriBooms",97.96
"Ancient Greek","PROIEL",98.17
"Ancient Greek","Perseus",90.04
"Ancient Hebrew","PTNK",91.63
"Arabic","PADT",93.64
"Armenian","BSUT",94.09
"Armenian","ArmTDP",94.90
"Basque","bdt",96.61
"Belarusian","HSE",94.61
"Bulgarian","BTB",97.54
"Catalan","AnCora",99.19
"Chinese (Simplified)","GSDSimp",92.49
"Chinese (Traditional)","gsd",92.28
"Classical Chinese","Kyoto",95.06
"Coptic","Scriptorium",86.14
"Croatian","SET",96.82
"Czech","FicTree",98.37
"Czech","CAC",97.59
"Czech","CLTT",95.62
"Czech","PDT",98.71
"Danish","DDT",96.09
"Dutch","Alpino",94.70
"Dutch","Lassysmall",94.96
"English","Atis",99.57
"English","EWT",95.69
"English","GUM",97.56
"English","LinES",97.80
"English","ParTUT",97.08
"French","GSD",97.90
"French","ParTUT",96.58
"French","Rhapsodie",96.37
"French","Sequoia",97.97
"French","ParisStories",95.94
"Estonian","EDT",96.17
"Estonian","EWT",91.64
"Finnish","FTB",96.39
"Finnish","TDT",94.98
"Gothic","PROIEL",96.88
"Greek","GDT",96.51
"Galician","CTG",97.78
"German","GSD",96.56
"German","HDT",95.86
"Hindi","HDTB",98.70
"Hebrew","IAHLTwiki",91.49
"Hebrew","HTB",89.14
"Hungarian","Szeged",93.90
"Irish","twittirish",87.35
"Irish","IDT",95.55
"Icelandic","GC",89.17
"Icelandic","IcePaHC",95.39
"Icelandic","Modern",94.95
"Indonesian","GSD",97.96
"Italian","postwita",95.96
"Italian","ParTUT",97.29
"Italian","MarkIT",86.01
"Italian","ISDT",97.99
"Italian","VIT",97.76
"Italian","twittiro",91.50
"Japanese","GSD",95.03
"Japanese","GSDLUW",91.96
"Korean","Kaist",93.45
"Korean","GSD",93.43
"Latin","PROIEL",96.82
"Latin","LLCT",98.52
"Latin","UDante",86.83
"Latin","ITTB",98.54
"Latvian","LVTB",96.26
"Lithuanian","ALKSNIS",92.71
"Maghrebi Arabic","Arabizi",52.05
"Marathi","UFAL",76.72
"Naija","NSC",99.26
"Norwegian","Bokmaal",97.91
"Norwegian","Nynorsk",97.50
"Old Church Slavonic","PROIEL",96.30
"Old East Slavic","Birchbark",76.47
"Old East Slavic","RNC",82.58
"Old East Slavic","TOROT",94.47
"Persian","PerDT",98.46
"Persian","Seraji",98.00
"Portuguese","Bosque",97.81
"Portuguese","CINTIL",97.96
"Portuguese","PetroGold",98.81
"Pomak","Philotis",98.28
"Polish","LFG",96.76
"Polish","PDB",97.25
"Romanian","Nonstandard",94.93
"Romanian","RRT",97.38
"Romanian","simonero",98.68
"Russian","GSD",94.46
"Russian","Taiga",93.99
"Russian","SynTagRus",97.46
"Serbian","SET",96.79
"Scottish Gaelic","ARCOSG",96.19
"Spanish","AnCora",99.20
"Spanish","GSD",98.20
"Swedish","LinES",96.23
"Swedish","Talbanken",97.20
"Slovenian","SSJ",97.48
"Slovak","SNK",93.97
"Tamil","TTB",81.47
"Turkish German","SAGT",90.42
"Turkish","Atis",98.52
"Turkish","BOUN",91.02
"Turkish","FrameNet",93.39
"Turkish","IMST",94.96
"Turkish","Penn",94.21
"Turkish","kenet",93.31
"Turkish","Tourism",99.02
"Urdu","UDTB",97.16
"Ukrainian","IU",96.18
"Uyghur","UDT",95.31
"Vietnamese","VTB",87.55
"Western Armenian","ArmTDP",96.61
"Welsh","CCG",95.01
"Wolof","wtb",94.85



## Evaluated languages

In addition to the main Early Slavic treebanks, OldSlavicLemma was evaluated on the following **64 languages** and **115 treebanks** from Universal Dependencies:

- Afrikaans
- Ancient Greek
- Ancient Hebrew
- Arabic
- Armenian
- Basque
- Belarusian
- Bulgarian
- Catalan
- Chinese
- Classical Chinese
- Coptic
- Croatian
- Czech
- Danish
- Dutch
- English
- Estonian
- Finnish
- French
- Galician
- German
- Gothic
- Greek
- Hebrew
- Hindi
- Hungarian
- Icelandic
- Indonesian
- Irish
- Italian
- Japanese
- Korean
- Latin
- Latvian
- Lithuanian
- Maghrebi Arabic
- Marathi
- Naija
- Norwegian
- Old Church Slavonic
- Old East Slavic
- Persian
- Polish
- Pomak
- Portuguese
- Romanian
- Russian
- Scottish Gaelic
- Serbian
- Slovak
- Slovenian
- Spanish
- Swedish
- Tamil
- Turkish
- Turkish German
- Ukrainian
- Urdu
- Uyghur
- Vietnamese
- Welsh
- Western Armenian
- Wolof


## Installation

Clone the repository:

```bash
git clone https://github.com/usmannawaz01/OldSlavicLemma.git
cd OldSlavicLemma
```

Create a new Python environment, or activate an existing environment where you want to install OldSlavicLemma.

You can create a new environment

```bash
conda create -n oldslaviclemma python=3.10
conda activate oldslaviclemma
```

Create or activate a Python environment, then install the requirements:

```bash
pip install -r requirements.txt
```

Install the package in editable mode:

```bash
pip install -e .
```

After installation, the training command should be available:

```bash
oldslaviclemma-train --help
```

## Training a model

OldSlavicLemma can be trained on any Universal Dependencies treebank that contains train, dev, and test `.conllu` files.

Example for **Old Church Slavonic — PROIEL**:

```bash
oldslaviclemma-train fit \
  --train UD_Old_Church_Slavonic-PROIEL/cu_proiel-ud-train.conllu \
  --dev UD_Old_Church_Slavonic-PROIEL/cu_proiel-ud-dev.conllu \
  --test UD_Old_Church_Slavonic-PROIEL/cu_proiel-ud-test.conllu \
  --output modelstore/cu_proiel \
  --model-id cu_proiel
```

On Windows CMD, use the same command on one line:

```cmd
oldslaviclemma-train fit --train UD_Old_Church_Slavonic-PROIEL/cu_proiel-ud-train.conllu --dev UD_Old_Church_Slavonic-PROIEL/cu_proiel-ud-dev.conllu --test UD_Old_Church_Slavonic-PROIEL/cu_proiel-ud-test.conllu --output modelstore/cu_proiel --model-id cu_proiel
```

The output folder will contain files such as:

```text
cuproielmodel.pt
vocab.json
config.json
registryentry.json
```

## Training on another UD treebank

To train on another treebank, replace the `--train`, `--dev`, and `--test` paths with the correct `.conllu` files.

Example for **Old East Slavic — TOROT**:

```bash
oldslaviclemma-train fit \
  --train UD_Old_East_Slavic-TOROT/orv_torot-ud-train.conllu \
  --dev UD_Old_East_Slavic-TOROT/orv_torot-ud-dev.conllu \
  --test UD_Old_East_Slavic-TOROT/orv_torot-ud-test.conllu \
  --output modelstore/orv_torot \
  --model-id orv_torot
```

On Windows CMD:

```cmd
oldslaviclemma-train fit --train UD_Old_East_Slavic-TOROT/orv_torot-ud-train.conllu --dev UD_Old_East_Slavic-TOROT/orv_torot-ud-dev.conllu --test UD_Old_East_Slavic-TOROT/orv_torot-ud-test.conllu --output modelstore/orv_torot --model-id orv_torot
```

## GPU training

The training code automatically uses GPU if PyTorch detects CUDA.

Check GPU availability with:

```bash
python -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NO GPU')"
```

If CUDA is available, training will print:

```text
Using device: cuda
```

Otherwise, it will run on CPU.




## Data

This repository does not include Universal Dependencies treebanks directly.

The experiments were run using **Universal Dependencies v2.12**. Users can download the required `.conllu` files from the official UD v2.12 release:

https://lindat.mff.cuni.cz/repository/items/9142eb95-44f7-442a-923f-0b39da4264fc

After downloading the treebanks, provide the paths to the train, dev, and test files using the `--train`, `--dev`, and `--test` arguments.

A typical project layout is:

```text
OldSlavicLemma/
├── oldslaviclemmatrain/
├── pyproject.toml
├── README.md
├── requirements.txt
└── UD_Old_Church_Slavonic-PROIEL/
    ├── cu_proiel-ud-train.conllu
    ├── cu_proiel-ud-dev.conllu
    └── cu_proiel-ud-test.conllu


```




## Evaluation settings

OldSlavicLemma can be evaluated in two settings.

### Gold-tokenization setting

Official UD tokenization and sentence boundaries are preserved. The model predicts lemmas for already-tokenized input.

**Metric:** accuracy

### Raw-tokenization setting

Raw input is first tokenized using an external tokenizer, and OldSlavicLemma is then used for lemma prediction.

**Metric:** Lemmas F1 score from the official CoNLL-2018 evaluation script

## Repository contents

This repository contains the source code required to train and export OldSlavicLemma models:

```text
oldslaviclemmatrain/
├── architecture.py
├── cli.py
├── conllu.py
├── dataset.py
├── examples.py
├── exporter.py
├── trainer.py
└── vocab.py
```

Main files:

- `cli.py` — command-line interface
- `trainer.py` — training loop
- `architecture.py` — neural model architecture
- `dataset.py` — PyTorch dataset and batching
- `conllu.py` — CoNLL-U reader
- `examples.py` — context-example creation
- `vocab.py` — character vocabulary
- `exporter.py` — model export utilities



## License

The source code in this repository is released under the MIT License.

The pretrained model weights are released separately under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

Commercial use of the pretrained model weights is not permitted without prior permission.


## Citation

A formal citation for `OldSlavicLemma` will be added soon.
