# Sorted Bar Plot

import matplotlib.pyplot as plt
countries = ["India", "USA", "China", "Japan", "Germany"]
gdp = [3.9, 29.1, 18.5, 4.2, 4.7]
data = list(zip(countries, gdp))
data.sort(key=lambda x: x[1], reverse=True)

countries = [i[0]for i in data]
gdp = [i[1] for i in data]

plt.bar(countries, gdp)
plt.title("GDP Comparison")
plt.ylabel("Trillion Dollars")

plt.show()