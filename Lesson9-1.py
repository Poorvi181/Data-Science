import pandas as pd

data = pd.read_csv("titanic.csv")
print(data.head())
print("\n--------------------------\n")
print(data.info())
print("\n--------------------------\n")
print(data.dtypes)

print("\n--------------------------\n")
nameandAge = data[["Name", "Age"]]
print(nameandAge.head())

print("\n--------------------------\n")
print(nameandAge.shape)

print("\n--------------------------\n")

print("\n----------------------------------------\n")
above35 = data[data["Age"] > 35]
print(above35.head())
print("\n----------------------------------------\n")
print(above35.shape)

print("\n----------------------------------------\n")
class2and3 = data[data["Pclass"].isin([2, 3])]
print(class2and3[["Name", "Pclass"]].head())
print("\n----------------------------------------\n")
print(class2and3.shape)

print("\n----------------------------------------\n")
class2and3 = data[(data["Pclass"] == 2) | (data["Pclass"] == 3)]
print(class2and3[["Name", "Pclass"]].head())
print("\n----------------------------------------\n")
print(class2and3.shape)
print("\n----------------------------------------\n")

print(maleFirstClass[["Name", "Sex", "Pclass", "Fare"]].head())
print("\n----------------------------------------\n")
print("Mean Fare of Male First Class Passengers:", maleFirstClass["Fare"].mean())

femaleFirstClass = data[(data["Sex"] == "female") & (data["Pclass"] == 1)]
maleSecondClass = data[(data["Sex"] == "male") & (data["Pclass"] == 2)]
femaleSecondClass = data[(data["Sex"] == "female") & (data["Pclass"] == 2)]
maleThirdClass = data[(data["Sex"] == "male") & (data["Pclass"] == 3)]
femaleThirdClass = data[(data["Sex"] == "female") & (data["Pclass"] == 3)]
print("Male First Class:", maleFirstClass["Fare"].mean())
print("Female First Class:", femaleFirstClass["Fare"].mean())
print("Male Second Class:", maleSecondClass["Fare"].mean())
print("Female Second Class:", femaleSecondClass["Fare"].mean())

print("Male Third Class:", maleThirdClass["Fare"].mean())

print("Female Third Class:", femaleThirdClass["Fare"].mean())
