import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix

salary_dataset = pd.read_csv("adult.csv")

salary_dataset.columns = [
    "age",
    "workclass",
    "final weight",
    ""
]