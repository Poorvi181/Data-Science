import pandas as pd
df = pd.DataFrame(
    {
        "Name":["Amelie", "Tom Brouwers"],
        "Age":[23,14],
        "City":["Chicago", "Amsterdam"]
    }
)
print(df.head())
print(df.shape)
print(df["Name"])
print(df["Age"].max())
print(type(df["Age"]))
print(df.info())
print(df.describe())