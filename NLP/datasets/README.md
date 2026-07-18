
# Natural Language Processing Datasets

This directory contains small text corpora used by the Natural Language Processing teaching notebooks.

The files support demonstrations of tokenization, text normalization, frequency analysis, Bag-of-Words, TF–IDF, word embeddings, language modelling, and text generation.

Third-party texts remain subject to their original licences and source conditions. The repository's MIT licence applies only to the original code and instructional documentation.

## Dataset Summary

| File | Content | Current status |
|---|---|---|
| `alice_in_wonderland.txt` | *Alice's Adventures in Wonderland* by Lewis Carroll | Included as an English literary corpus |
| `bible-kjv.txt` | King James Version Bible text | Source and notebook usage require confirmation |
| `bible.txt` | Alternative Bible text file | Difference from `bible-kjv.txt` requires confirmation |
| `covid.txt` | Intended COVID-related text sample | Currently empty or incomplete |

## `alice_in_wonderland.txt`

This file contains the English text of *Alice's Adventures in Wonderland* by Lewis Carroll.

The stored copy identifies itself as the Millennium Fulcrum Edition 3.0.

### Instructional uses

The corpus may be used to demonstrate:

- sentence and word tokenization;
- text normalization;
- vocabulary construction;
- word-frequency analysis;
- stop-word removal;
- Bag-of-Words representation;
- TF–IDF representation;
- Word2Vec training;
- CBOW and Skip-Gram examples;
- introductory language modelling;
- text-generation experiments.

### Provenance status

The literary work is in the public domain, but the exact source of this electronic edition should still be recorded.

Before final review, the repository should identify:

- the website or corpus from which the file was obtained;
- the date it was accessed;
- whether formatting or preprocessing was applied;
- which notebooks use the file.

## `bible-kjv.txt`

This file appears to contain an English King James Version Bible corpus.

Possible instructional uses include:

- tokenization;
- vocabulary and frequency analysis;
- n-gram examples;
- word-embedding demonstrations;
- comparison of language styles.

The exact electronic-text provider and redistribution terms must be confirmed.

## `bible.txt`

This file appears to be another Bible text corpus.

Before the cleanup branch is merged, it should be compared with `bible-kjv.txt` to determine:

- whether the text version is the same;
- whether the files differ only in formatting;
- whether both files are used by separate notebooks;
- whether one file is redundant;
- which source and licence apply.

A duplicate file should not remain without a documented teaching purpose.

## `covid.txt`

This file is currently empty or incomplete.

An empty dataset does not support a reproducible lesson. Before final review, it should either:

1. be populated with a clearly sourced and redistributable text sample; or
2. be removed from the repository.

Do not add copied news articles or website content without confirming that redistribution is permitted.

## Reproducible File Access

Notebooks should load text files using repository-relative paths.

For a notebook inside `NLP/notebooks`, use:

```python
from pathlib import Path

data_path = Path("../datasets/alice_in_wonderland.txt")
text = data_path.read_text(encoding="utf-8")
