# Artificial Intelligence and Machine Learning Teaching Portfolio

This repository presents a curated collection of Jupyter notebooks developed for teaching and demonstrating concepts in artificial intelligence, data science, machine learning, natural language processing, and computer vision.

The materials combine conceptual explanation, Python implementation, practical examples, visual analysis, and guided exercises. They are intended to demonstrate both technical knowledge and experience in developing instructional content.

## Subject Areas

| Directory                                             | Main topics                                                                                                                       |
| ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [`AI-Course`](AI-Course/)                             | Search algorithms, optimization, game-tree methods, decision trees, and neural-network fundamentals                               |
| [`Data-Science-Course`](Data-Science-Course/)         | Data analysis, statistical relationships, data manipulation, and visualization                                                    |
| [`Machine-Learning-Course`](Machine-Learning-Course/) | Regression, classification, regularization, model evaluation, and deep learning                                                   |
| [`NLP`](NLP/)                                         | Text representation, word embeddings, classification, sentiment analysis, pretrained language models, and Transformer fine-tuning |
| [`computer-vision`](computer-vision/)                 | Image representation, image processing, deep-learning applications, and object detection                                          |

Each subject directory contains instructional notebooks and, where required, small datasets used in the corresponding examples.

## Teaching Approach

The notebooks generally follow an implementation-oriented sequence:

1. Introduce the problem and its underlying concept.
2. Explain the relevant algorithm or model.
3. Implement the method using Python.
4. Apply it to a practical example or dataset.
5. inspect and interpret the resulting output.
6. Discuss limitations, parameter choices, or possible extensions.

Some notebooks implement algorithms manually to clarify their internal operation. Others use established Python libraries to demonstrate practical workflows.

## Repository Structure

```text
.
├── AI-Course/
│   ├── notebooks/
│   ├── datasets/
│   └── README.md
├── Data-Science-Course/
│   ├── notebooks/
│   ├── datasets/
│   └── README.md
├── Machine-Learning-Course/
│   ├── notebooks/
│   ├── datasets/
│   └── README.md
├── NLP/
│   ├── notebooks/
│   ├── datasets/
│   └── README.md
├── computer-vision/
│   └── notebooks/
└── README.md
```

## Topics Demonstrated

The repository includes examples covering:

* classical artificial-intelligence search;
* numerical and heuristic optimization;
* exploratory data analysis;
* supervised and unsupervised learning;
* regression and classification;
* regularization and hyperparameter selection;
* neural networks and deep learning;
* natural language preprocessing;
* Bag-of-Words and TF–IDF representations;
* Word2Vec, CBOW, and Skip-Gram;
* text classification and sentiment analysis;
* pretrained language models;
* Transformer fine-tuning;
* image processing and computer vision;
* object-detection workflows.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/emansafwatm/Python-Code.git
cd Python-Code
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install JupyterLab:

```bash
python -m pip install --upgrade pip
pip install jupyterlab
```

Launch JupyterLab:

```bash
jupyter lab
```

Open the relevant subject directory and follow the notebook sequence documented in its README.

Individual notebooks may require additional libraries such as:

* NumPy
* Pandas
* Matplotlib
* scikit-learn
* TensorFlow or Keras
* PyTorch
* NLTK
* Gensim
* Hugging Face Transformers
* OpenCV

The required packages are identified within the relevant notebook or subject documentation.

## NLP Transformer Example

The NLP section includes a compact example of fine-tuning a pretrained Transformer for sentiment classification.

The lesson demonstrates:

* tokenization;
* attention masks;
* PyTorch datasets and data loaders;
* loading a pretrained BERT model;
* loss calculation;
* backpropagation;
* model evaluation;
* prediction;
* saving the fine-tuned model.

The example is intentionally small and self-contained so that the complete training workflow can be inspected without requiring a research-scale dataset.

## Dataset Use

Datasets included in the repository are used for instructional demonstrations. Dataset directories should document the source, purpose, and any preprocessing applied.

External datasets, corpora, and pretrained models remain subject to their original licences and usage conditions.

## Intended Use

This repository serves as:

* a teaching portfolio;
* supporting material for classroom and laboratory instruction;
* a collection of practical AI and machine-learning examples;
* a reference for students and independent learners;
* evidence of curriculum development and technical instruction.

The notebooks are educational implementations. Research-specific experimental code is maintained in the corresponding research repositories.

## Author

**Eman Khater**

AI researcher and instructor with interests in large language models, natural language processing, machine translation, high-performance computing, model optimization, and applied artificial intelligence.

## Contributions

Corrections, suggestions, and constructive improvements are welcome through GitHub issues or pull requests.

