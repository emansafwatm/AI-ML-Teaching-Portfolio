# Modernized Machine Learning Course Notebooks

This package contains 14 standardized notebooks derived from the uploaded course materials.

## Included Improvements

- Consistent lesson numbering and course navigation
- Learning objectives, prerequisites, review exercises, and references
- Cleared stale outputs and execution counts
- Updated removed `predict_classes` usage
- Removed deprecated estimator-level `normalize=True`
- Corrected the Reuters multiclass loss/metric configuration
- Rebuilt the Underfitting and Overfitting lesson as a complete reproducible notebook
- Added fixed-seed and pipeline-oriented reproducibility guidance

## Important Execution Notes

The notebooks retain the original datasets and instructional examples. Some require local files such as:

- `Car_Data.csv`
- `drug200_v2.csv`
- `kc_house_data.csv`
- `bank.csv` or the bank-note dataset used by the original notebook

Place the notebooks in `Machine-Learning-Course/notebooks/` and retain the repository's dataset directory structure.

Deep-learning notebooks may download public Keras datasets when first executed and therefore require internet access. Run each notebook with **Restart Kernel and Run All Cells** after installing the project dependencies.

## Recommended Course Order

1. Linear Algebra
2. Linear Regression
3. Polynomial Regression
4. Underfitting and Overfitting
5. L1 and L2 Regularization
6. Ridge and Lasso Regression
7. K-Nearest Neighbors
8. Support Vector Machines
9. Breast Cancer SVM Classification
10. Drug Classification Model Comparison
11. Bank Classification Model Comparison
12. Hyperparameter Optimization
13. Keras Basics
14. Deep Learning
