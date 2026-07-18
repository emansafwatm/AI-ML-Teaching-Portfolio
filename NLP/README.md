# Natural Language Processing Course

This directory contains instructional materials covering foundational and modern natural language processing methods.

The lessons progress from text preprocessing and statistical text representation to word embeddings, text classification, pretrained language models, Transformer fine-tuning, and text generation.

## Learning Objectives

After completing the materials, students should be able to:

- preprocess and tokenize text;
- construct Bag-of-Words and TF–IDF representations;
- explain sparse and dense text representations;
- train and interpret Word2Vec models;
- distinguish CBOW from Skip-Gram;
- prepare data for text-classification tasks;
- build and evaluate sentiment-analysis workflows;
- use pretrained models from Hugging Face;
- explain Transformer pretraining and fine-tuning;
- fine-tune a compact BERT model;
- generate text using a pretrained GPT-2 model;
- discuss the limitations of small teaching datasets and pretrained models.

## Directory Structure

```text
NLP/
├── README.md
├── datasets/
│   ├── README.md
│   ├── alice_in_wonderland.txt
│   ├── bible-kjv.txt
│   ├── bible.txt
│   └── covid.txt
└── notebooks/
    ├── README.md
    ├── tokenizer.ipynb
    ├── Bag_of_Words_Model.ipynb
    ├── TF_IDF.ipynb
    ├── Word2Vec.ipynb
    ├── CBOW_Continuous_Bag_of_Words2.ipynb
    ├── Skip_Gram_Model.ipynb
    ├── Classification.ipynb
    ├── Sentiment_Analysis.ipynb
    ├── HuggingFace.ipynb
    ├── transformer_fine_tuning_example.ipynb
    └── Text_gen_gpt2.ipynb
