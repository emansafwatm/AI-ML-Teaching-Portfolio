
# Machine Learning Course Datasets

This directory contains datasets used by the instructional notebooks in the Machine Learning course.

The datasets support demonstrations of classification, regression, preprocessing, model comparison, and evaluation. They are included for educational use where appropriate.

Third-party datasets remain governed by their original licences and usage conditions. The repository's MIT licence applies only to the original code and instructional material.

## Dataset Summary

| Dataset | Learning task | Target variable |
|---|---|---|
| `bank.csv` | Binary classification | `deposit` |
| `Car_Data.csv` | Binary classification | `Purchased` |
| `kc_house_data.csv` | Regression | `price` |
| `kc_house_data1.csv` | Regression | `price` |

## `bank.csv`

This dataset contains customer and marketing-campaign attributes used to demonstrate binary classification.

### Main fields

| Field | Description |
|---|---|
| `age` | Customer age |
| `job` | Employment category |
| `marital` | Marital status |
| `education` | Education category |
| `default` | Credit-default indicator |
| `balance` | Account balance |
| `housing` | Housing-loan indicator |
| `loan` | Personal-loan indicator |
| `contact` | Contact method |
| `day` | Day of contact |
| `month` | Month of contact |
| `duration` | Contact duration |
| `campaign` | Number of campaign contacts |
| `pdays` | Days since a previous contact |
| `previous` | Number of previous contacts |
| `poutcome` | Outcome of the previous campaign |
| `deposit` | Binary classification target |

### Instructional uses

The dataset supports demonstrations of:

- inspecting numerical and categorical features;
- encoding categorical variables;
- separating features and labels;
- stratified train/test splitting;
- classification-model comparison;
- confusion-matrix analysis;
- accuracy, precision, recall, and F1-score.

## `Car_Data.csv`

This dataset contains demographic attributes used to predict whether a user purchased a product.

### Main fields

| Field | Description |
|---|---|
| `User ID` | Record identifier |
| `Gender` | User gender category |
| `Age` | User age |
| `EstimatedSalary` | Estimated salary |
| `Purchased` | Binary classification target |

### Instructional uses

The dataset may be used to demonstrate:

- feature selection;
- categorical encoding;
- feature scaling;
- train/test splitting;
- K-Nearest Neighbors;
- Support Vector Machines;
- binary-classification evaluation.

`User ID` is an identifier and should normally be excluded from model training.

## `kc_house_data.csv`

This dataset contains residential-property characteristics used to predict sale prices.

### Main fields

| Field | Description |
|---|---|
| `id` | Property identifier |
| `date` | Sale date |
| `price` | Regression target |
| `bedrooms` | Number of bedrooms |
| `bathrooms` | Number of bathrooms |
| `sqft_living` | Interior living area |
| `sqft_lot` | Lot area |
| `floors` | Number of floors |
| `waterfront` | Waterfront indicator |
| `view` | View rating |
| `condition` | Property-condition rating |
| `grade` | Construction and design grade |
| `sqft_above` | Above-ground living area |
| `sqft_basement` | Basement area |
| `yr_built` | Construction year |
| `yr_renovated` | Renovation year |
| `zipcode` | Postal code |
| `lat` | Latitude |
| `long` | Longitude |
| `sqft_living15` | Nearby living-area measure |
| `sqft_lot15` | Nearby lot-area measure |

### Instructional uses

The dataset supports demonstrations of:

- exploratory data analysis;
- correlation analysis;
- linear regression;
- polynomial regression;
- Ridge and Lasso regression;
- feature selection;
- regression-error metrics;
- underfitting and overfitting.

## `kc_house_data1.csv`

This file has the same general schema and target variable as `kc_house_data.csv`, but it contains a different number of records.

It should be treated as a separate prepared version until its preprocessing history is confirmed.

Before the repository is merged into `main`, we should determine:

- which notebook uses each house-price file;
- whether rows were removed or filtered;
- whether missing values were treated;
- whether one file is an intermediate version;
- whether both files are necessary.

A redundant or undocumented copy should not remain in the final teaching portfolio.

## Drug Classification Dataset

The files:

```text
../notebooks/drug200.csv
../notebooks/drug200_v2.csv
