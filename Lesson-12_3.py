import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
print(df.head())
print("\nNumber of passengers:", len(df))
print("\nColumns:")
print(df.columns)
plt.figure(figsize=(14,10))
plt.subplot(2, 3, 1)
survival_counts=df["Survived"].value_counts()
plt.bar(
    ["Did Not Survive", "Survived"],
    [survival_counts.get(0, 0), survival_counts.get(1,0)]
)
plt.title("Survival Count")
plt.xlabel("Survival Status")
plt.ylabel("Number of Passengers")

plt.subplot(2 ,3, 2)
survival_counts = df["Survived"].value_counts()

plt.pie(
    survival_counts,
    labels = ["Did Not Survive", "Survived"],
    autopct = "%1.1f%%"
    startangle = 90
)

plt.title("Survival Percentage")

plt.subplot(2, 3, 3)
plt.hist(df["Age"].dropna(), bins = 10)

plt.title("Age Distrubution")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")

plt.subplot(2, 3, 4)
age_fare = df[["Age", "Fare"]].dropna()
plt.scatter(age_fare["Age"], age_fare["Fare"])

plt.itle("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")

plt.subplot(2, 3, 5)
class_counts = df["Pclass"].value_counts().sort_index()
plt.plot(class_counts.index, class_counts.values,marker="o")
plt.title("Passengers by class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")

plt.subplot(2, 3, 6)
class_numbers = [1, 2, 3]
male_counts = []
female_counts = []

