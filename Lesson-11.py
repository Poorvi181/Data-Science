#Equation:
#y = x²

import matplotlib.pyplot as plt

x = []
y = []

for i in range(-10, 11):
    x.append(i)
    y.append(i*i)

plt.plot(x,y)
plt.grid()
plt.show()

#Using NumPy for Smooth Curve

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = x**2
plt.plot(x, y)
plt.grid()
plt.show()

#Bar Plot with Colours
import matplotlib.pyplot as plt

students = ["Ali", "Sara", "John", "Emma"]
marks = [80, 92, 75, 88]
plt.bar(students, marks, color="green")
plt.show()

#Bar Plot with Lables
import matplotlib.pyplot as plt

fruits = ["Apple", "Banana", "Orange", "Mango"]
quantity = [25, 40, 18, 30]
plt.bar(fruits, quantity)
plt.title("Fruit Sales")
plt.xlabel("Fruits")
plt.ylabel("Quantity Sold")
plt.show()

#21. Horizontal Bar Plot
import matplotlib.pyplot as plt

languages = ["Python", "Java", "C++", "JavaScript"]
students = [50, 35, 25, 40]
plt.barh(languages, students)
plt.title("Programming Language Popularity")
plt.show()

#22. Bar Plot with Different Colors 
import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Tablet", "Watch"]
sales = [45, 70, 35, 55]
colors = ["red", "blue", "green", "orange"]
plt.bar(products, sales, color=colors)
plt.show()