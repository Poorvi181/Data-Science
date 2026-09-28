import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
products = ["A", "B", "C", "D"]
sales = [40, 60, 30, 80]
ages = [10, 11, 12, 12 ,13, 13]
study_hours = [1, 2, 3, 4, 5]
scores = [40,50, 60, 75, 90]
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.subplot(2, 2, 2)
plt.bar(products, sales)
plt.title("Bar Chart")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.subplot(2, 2, 3)
plt.hist(ages, bins=5)
plt.title("Histogram")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.subplot(2, 2, 4)
plt.scatter(study_hours, scores)
plt.title("Scatter Plot")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.tight_layout()
plt.show()