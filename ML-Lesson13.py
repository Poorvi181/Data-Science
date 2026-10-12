# Machine Learning Project- Titanic CSV
# Titanic Survival Prediction

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("titanic.csv")
data.colums = data.columns.str.strip()
print("Columns in dataset: ")
print(data.columns.tolist())
print("\nFirst 5 rows: ")
print(data.head())
print("\nMissing values before preprocessing: ")
print(data.isnull().sum())
average_age = data["Age"].mean()
print("\nAverage Age:", average_age)
data["Age"] = data["Age"].fillna(average_age)

if "Embarked" not in data.columns:
    print("\nEmbarked column was not found.")
    print("Creating an Embarked column with 'Unknown'.")
    data["Embarked"] = "Unknown"

most_common_embarked = data["Embarked"].mode()[0]
print("\nMost common Embarked value:" , most_common_embarked)
data["Embarked"] = data["Embarked"].fillna(most_common_embarked)
data["Sex"] = data["Sex"] .str.strip().str.lower()
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})
data["Embarked"] = data["Embarked"].astype(str)
data["Embarked"] = data["Embarked"].str.strip().str.upper()
data["Embarked"] = data["Embarked"].map({
    "S": 0,
    "C": 1,
    "Q": 2,
    "UNKNOWN": 3
})

print("\nData after preprocessing: ")
print(data.head())
print("\nMissing values after preprocessing: ")
print(data.isnull().sum())
X = data[["Pclass", "Sex", "Age", "Fare", "Embarked"]]
Y = data["Survived"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_train))
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)
print("\nModel training completed!")

        

