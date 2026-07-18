# Natural Language Processing Notebooks

This directory contains instructional notebooks covering foundational and modern natural language processing techniques.

The notebooks are intended for classroom demonstrations, guided laboratory sessions, and independent practice. They progress from traditional text representations to neural language models and pretrained Transformers.

## Learning objectives

After completing the notebooks, students should be able to:

* preprocess and tokenize textual data;
* construct Bag-of-Words and TF–IDF representations;
* explain distributed word representations;
* train and interpret Word2Vec models;
* distinguish between CBOW and Skip-Gram architectures;
* build basic text-classification and sentiment-analysis pipelines;
* use pretrained models from Hugging Face;
* explain the difference between Transformer pretraining and fine-tuning;
* fine-tune a compact Transformer for text classification;
* generate text using a pretrained GPT-2 model.

## Recommended notebook sequence

| Order | Notebook                                | Main topic                                |
| ----: | --------------------------------------- | ----------------------------------------- |
|     1 | `tokenizer.ipynb`                       | Text tokenization and preprocessing       |
|     2 | `Bag_of_Words_Model.ipynb`              | Bag-of-Words text representation          |
|     3 | `TF_IDF.ipynb`                          | Term Frequency–Inverse Document Frequency |
|     4 | `Word2Vec.ipynb`                        | Distributed word representations          |
|     5 | `CBOW_Continuous_Bag_of_Words2.ipynb`   | Continuous Bag-of-Words training          |
|     6 | `Skip_Gram_Model.ipynb`                 | Skip-Gram training                        |
|     7 | `Classification.ipynb`                  | Text-classification workflow              |
|     8 | `Sentiment_Analysis.ipynb`              | Sentiment-analysis application            |
|     9 | `HuggingFace.ipynb`                     | Using pretrained Hugging Face models      |
|    10 | `transformer_fine_tuning_example.ipynb` | Fine-tuning a small BERT model            |
|    11 | `Text_gen_gpt2.ipynb`                   | Text generation with GPT-2                |

## Transformer fine-tuning lesson

`transformer_fine_tuning_example.ipynb` provides a compact, self-contained demonstration of fine-tuning a pretrained Transformer.

The notebook covers:

* loading a pretrained BERT tokenizer and model;
* converting text into input IDs and attention masks;
* constructing PyTorch datasets and data loaders;
* implementing a standard training loop;
* calculating classification loss;
* performing backpropagation and parameter updates;
* evaluating predictions;
* saving the fine-tuned model and tokenizer.

The notebook uses a deliberately small teaching dataset and a compact BERT model so that students can inspect the complete workflow without requiring a large research dataset or extensive computational resources.

This notebook is educational material and was not used to generate results for a research publication.

## Requirements

The notebooks use a combination of the following libraries:

```bash
numpy
pandas
matplotlib
scikit-learn
nltk
gensim
torch
transformers
datasets
```

Individual notebooks may require only a subset of these packages.

Some pretrained-model notebooks require an internet connection during their first execution to download model weights and tokenizer files.

## Dataset notes

Small teaching datasets may be included in the adjacent `datasets` directory. Each dataset should be used only for the lesson for which it is documented.

External corpora and pretrained models remain subject to their original licences and usage conditions.

## Execution guidance

For the intended learning experience:

1. Read the introductory Markdown before running the code.
2. Execute the cells in order.
3. Examine intermediate representations and tensor dimensions.
4. Compare model outputs with the expected labels or text.
5. Complete the exercises provided at the end of the relevant notebook.

The examples are designed to explain methods and workflows. Results obtained from the small teaching datasets should not be interpreted as production-level model performance.

