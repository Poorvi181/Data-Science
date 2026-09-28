import pandas as pd 
import matplotlib.pylot as plt

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