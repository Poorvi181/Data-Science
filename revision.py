import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("air_quality.csv")
df["datetime"] = pd.to_datetime(df["datetime"])
print(df.head())
print("\nSHAPE:", df.shape)
print("\nINFO:")
df.info()
print("\nSUMMARY\n", df.describe())
print("\nMISSING VALUES\n", df.isnull().sum())

numeric_cols = ["CO_mg_m3", "NO2_ug_m3", "benzene_ug_m3", "temperature_c", "humidity_pct"]
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

df["hour"] = df["datetime"].dt.hour
df["pollution_level"] = np.where(df["NO2_ug_m3"] > df["NO2_ug_m3"].median(), "Higher", "Lower")
print("\nAVERAGE POLLUTANTS\n", df[["CO_mg_m3", "NO2_ug_m3","benzene_ug_m3"]].mean())
print("\nHOURLY NO2 AVERAGE\n", df.groupby("hour")["NO2_ug_m3"].mean())

co = df["CO_mg_m3"].to_numpy()
print("\nNUMPY CO MEAN:", np.mean(co))
print("NUMPY CO MEDIAN:", np.median(co))
print("NUMPY CO STD:", np.std(co))
print("CO ABOVE 75th PERCENTILE:", np.sum(co > np.percentile(co, 75)))

df.set_index("datetime")["NO2_ug_m3"].plot(figsize=(11,5), title="Nitrogen Dioxide Over Time")
plt.ylabel("NO2 (ug/m3)")
plt.tight_layout()
plt.show()

sns.scatterplot(data = df, x="temperature_c", y="NO2_ug_m3", hue="pollution_level")
plt.title("Temperature vs NO2")
plt.tight_layout()
plt.show()

sns.histplot(data=df, x="CO_mg_m3", bins=25, kde=True)
plt.title("Carbon Monoxide Distrubution")
plt.tight_layout()
plt.show()

sns.boxplot(data=df, x="pollution_level", y="benzene_ug_m3")
plt.title("Benzene by Pollution Category")
plt.tight_layout()
plt.show()

sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm")
plt.title("Air Quality Correlation Heatmap")
plt.tight_layout()
plt.show()