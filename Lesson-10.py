#Line Plot

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 20, 18]

plt.plot(x, y)
plt.show()

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 120, 140, 130, 170]

plt.plot(months, sales, color = "red", linestyle = "--",
         marker = "o", linewidth = 5, markersize = 8)
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid()
plt.show()




# Change axis limits

x = [1, 2, 3, 4, 5]
y = [20, 30, 25, 35, 40]

plt.plot(x, y)
plt.axis([0, 6, 0, 50])
plt.show()

# Use xlim() and ylim()

x = [1, 2, 3, 4, 5]
y = [20, 30, 25, 35, 40]

plt.plot(x, y)
plt.xlim(0, 6)
plt.ylim(0, 60)
plt.show()

#Multple line plots

months = [1, 2, 3, 4, 5]
sales = [100, 120, 150, 170, 200]
profit = [20, 25, 35, 40, 55]
plt.plot(months, sales, label="sales")
plt.plot(months, profit, label="Profit")
plt.legend()
plt.show()

# Equation:
# y = 2x + 1

import matplotlib.pyplot as plt

x = []
y = []

for i in range(-5, 6):
x.append(i)
y.append(2 * i + 1)

plt.plot(x, y)

plt.grid()

plt.show()