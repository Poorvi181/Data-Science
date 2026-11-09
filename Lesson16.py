import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix

salary_dataset = pd.read_csv("adult.csv")

salary_dataset.columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "educational-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "gender",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "income",
]

salary_dataset.rename(
    columns={
        "capital-gain": "capital gain",
        "capital-loss": "capital loss",
        "native-country": "country",
        "hours-per-week": "hours per week",
        "marital-status": "marital",
    },
    inplace = True,
)
print(salary_dataset.describe())
print(salary_dataset.info())
print(salary_dataset.isnull().sum())
print(salary_dataset.isin(["?"]).sum(axis=0))
for c in salary_dataset.columns:
    print("----%s----"% c)
    print(salary_dataset[c].value_counts())

salary_dataset.drop(
    [
        "educational-num",
        "age",
        "hours per week",
        "fnlwgt",
        "capital gain",
        "capital loss",
        "country",
    ],
    axis=1,
    inplace=True,

)
income = set(salary_dataset["income"])
print(income)
salary_dataset["income"] = (
    salary_dataset["income"].map({" <=50K": 0, " >50K": 1}).astype(int)
)
salary_dataset.head()
salary_dataset["gender"] = (
    salary_dataset["gender"].map({" Male":0, " Female": 1}).astype(int)
)

salary_dataset["race"] = (
    salary_dataset["race"]
    .map(
        {
            " Black": 0,
            " Asian-Pac-Islander": 1,
            " Other": 2,
            " White": 3,
            " Amer-Indian-Eskimo": 4,
        }
    )
    .astype(int)
)

salary_dataset["marital"]=(
    salary_dataset["marital"]
    .map(
        {
            " Married-spouse-absent": 0,
            " Widowed": 1,
            " Married-civ-spouse": 2,
            " Seperated": 3,
            " Divorced": 4,
            " Never-married": 5,
            " Married-AF-spouse": 6,
        }
    )
    .astype(int)
)

salary_dataset["relationship"] = (
    salary_dataset["relationship"]
    .map(
        {
            " Not-in-family": 0,
            " Wife": 1,
            " Other-relative": 2, 
            " Unmarried": 3,
            " Husband": 4,
            " Own-child": 5,
        }
    )
    .astype(int)
)

salary_dataset.groupby("education").income.mean().plot(kind="bar")
plt.show()

salary_dataset.groupby("occupation").income.mean().plot(kind="bar")
plt.show()

salary_dataset.groupby("relationship").income.mean().plot(kind="bar")
plt.show()

salary_dataset.groupby("race").income.mean().plot(kind="bar")
plt.show()

salary_dataset.groupby("gender").income.mean().plot(kind="bar")
plt.show()

salary_dataset.groupby("workclass").income.mean().plot(kind="bar")
plt.show()

salary_dataset.groupby("marital").income.mean().plot(kind="bar")
plt.show()