
# Artificial Intelligence Course Datasets

This directory contains datasets used by the instructional notebooks in the Artificial Intelligence course.

The files support demonstrations of classification, neural networks, decision trees, probabilistic learning, model evaluation, and data preprocessing.

Third-party datasets remain governed by their original licences and source conditions. The repository's MIT licence applies only to the original code and instructional documentation.

## Dataset Summary

| Dataset | Learning task | Target |
|---|---|---|
| `User_Data.csv` | Binary purchase classification | `Purchased` |
| `diabetes2.csv` | Binary diabetes classification | Final column |
| `har_train.csv` | Wearable-sensor movement classification | `classe` |
| `har_validate.csv` | Validation data for wearable-sensor classification | `classe` |
| `iris_train.csv` | Iris species classification | `Species` |
| `iris_test.csv` | Test data for Iris species classification | `Species` |

## `User_Data.csv`

This dataset contains demographic variables used to predict whether a user purchased a product.

### Fields

| Field | Description |
|---|---|
| `User ID` | Record identifier |
| `Gender` | User gender category |
| `Age` | User age |
| `EstimatedSalary` | Estimated salary |
| `Purchased` | Binary classification target |

### Instructional uses

The dataset may be used to demonstrate:

- categorical-variable encoding;
- feature selection;
- train/test splitting;
- feature scaling;
- classification;
- confusion-matrix analysis;
- accuracy, precision, recall, and F1-score.

`User ID` is an identifier and should normally be excluded from model training.

## `diabetes2.csv`

This dataset contains nine numerical columns commonly used for binary diabetes classification.

The expected columns are:

| Position | Expected field |
|---:|---|
| 1 | Pregnancies |
| 2 | Glucose |
| 3 | Blood pressure |
| 4 | Skin thickness |
| 5 | Insulin |
| 6 | Body mass index |
| 7 | Diabetes pedigree function |
| 8 | Age |
| 9 | Outcome |

### Current formatting issue

The file currently has no descriptive CSV header row. Consequently, software may interpret the first patient record as the column names.

Until the file is corrected, it should be loaded explicitly with column names:

```python
from pathlib import Path
import pandas as pd

column_names = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
    "Outcome",
]

data_path = Path("../datasets/diabetes2.csv")

diabetes_data = pd.read_csv(
    data_path,
    header=None,
    names=column_names,
)
