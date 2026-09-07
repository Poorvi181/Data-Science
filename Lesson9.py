import pandas as pd

weather_data = {
    "City": ["Chicago", "Los Angles", "London", "Manchester", "Miami"],
    "Temperature": [32, 21, 28, 25, 20],
    "Humidity": [75, 45, 70, 30, 65],
    "Rainfall": [220, 80, 180, 20, 150],
}

df = pd.DataFrame(weather_data)

print("City Weather Dataset")
print(df)

max_temp = df["Temperature"].max()

hottest_city = df[df["Temperature"] == max_temp]
print(hottest_city[["City", "Temperature"]])

avg_rainfall = df["Rainfall"].mean()
print("\nAverage Rainfall: ", avg_rainfall)

hot_cities = df[df["Temperature"] > 30]
print("\nCities with temprature greater than 30 C: ")
print(hot_cities)