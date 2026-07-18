
# Machine Learning Course

This directory contains instructional notebooks covering the mathematical foundations, implementation, evaluation, and practical application of machine-learning methods.

The materials progress from linear algebra and regression to classification, regularization, model comparison, hyperparameter optimization, and introductory deep learning.

## Learning Objectives

After completing these notebooks, students should be able to:

- explain the basic mathematical foundations of machine learning;
- prepare data for supervised-learning tasks;
- distinguish regression from classification;
- implement linear and polynomial regression;
- explain underfitting and overfitting;
- apply L1 and L2 regularization;
- use Ridge and Lasso regression;
- train K-Nearest Neighbors and Support Vector Machine models;
- compare multiple classification algorithms;
- evaluate models using appropriate performance metrics;
- perform hyperparameter optimization;
- explain the basic structure of neural networks;
- construct introductory models using Keras;
- interpret results and identify methodological limitations.

## Notebook Topics

### Mathematical Foundations

| Notebook | Main topic |
|---|---|
| `Linear_Algebra.ipynb` | Vectors, matrices, and linear-algebra operations used in machine learning |

### Regression

| Notebook | Main topic |
|---|---|
| `Linear_Regression.ipynb` | Linear-regression concepts and implementation |
| `Polynomial_Regression.ipynb` | Modelling nonlinear relationships using polynomial features |
| `Ridge_and_Lasso_Regression.ipynb` | Regularized regression using Ridge and Lasso |
| `L1_and_L2_regularization.ipynb` | Comparison of L1 and L2 regularization |
| `Underfitting_and_Overfitting.ipynb` | Model complexity, bias, variance, and generalization |

### Classification

| Notebook | Main topic |
|---|---|
| `KNN_algorithm.ipynb` | K-Nearest Neighbors classification |
| `Support_Vector_Machine.ipynb` | Support Vector Machine fundamentals |
| `Breast_Cancer_SVM_Classification.ipynb` | Binary classification using a Support Vector Machine |
| `Drug_Classification_Model_Comparison.ipynb` | Comparison of classification models using a drug dataset |
| `Bank_Classification_Model_Comparison.ipynb` | Comparison of classification models using banking data |

### Model Selection and Optimization

| Notebook | Main topic |
|---|---|
| `Hyperparameter_Optimization.ipynb` | Hyperparameter search and model tuning |

### Neural Networks and Deep Learning

| Notebook | Main topic |
|---|---|
| `Keras_Basics.ipynb` | Introduction to model construction using Keras |
| `Deep_Learning.ipynb` | Introductory deep-learning workflow |

## Suggested Study Sequence

A suitable sequence is:

1. `Linear_Algebra.ipynb`
2. `Linear_Regression.ipynb`
3. `Polynomial_Regression.ipynb`
4. `Underfitting_and_Overfitting.ipynb`
5. `L1_and_L2_regularization.ipynb`
6. `Ridge_and_Lasso_Regression.ipynb`
7. `KNN_algorithm.ipynb`
8. `Support_Vector_Machine.ipynb`
9. `Breast_Cancer_SVM_Classification.ipynb`
10. `Drug_Classification_Model_Comparison.ipynb`
11. `Bank_Classification_Model_Comparison.ipynb`
12. `Hyperparameter_Optimization.ipynb`
13. `Keras_Basics.ipynb`
14. `Deep_Learning.ipynb`

## Directory Structure

```text
Machine-Learning-Course/
├── README.md
├── datasets/
│   ├── README.md
│   ├── bank.csv
│   ├── Car_Data.csv
│   ├── kc_house_data.csv
│   └── kc_house_data1.csv
└── notebooks/
    ├── Linear_Algebra.ipynb
    ├── Linear_Regression.ipynb
    ├── Polynomial_Regression.ipynb
    ├── Underfitting_and_Overfitting.ipynb
    ├── L1_and_L2_regularization.ipynb
    ├── Ridge_and_Lasso_Regression.ipynb
    ├── KNN_algorithm.ipynb
    ├── Support_Vector_Machine.ipynb
    ├── Breast_Cancer_SVM_Classification.ipynb
    ├── Drug_Classification_Model_Comparison.ipynb
    ├── Bank_Classification_Model_Comparison.ipynb
    ├── Hyperparameter_Optimization.ipynb
    ├── Keras_Basics.ipynb
    └── Deep_Learning.ipynb
