import numpy as np
import matplotlib.pyplot as plt

m1 = float(input("Enter m for line 1: "))
c1 = float(input("Enter c for line 1: "))

m2 = float(input("Enter m for line 2: "))
c2 = float(input("Enter c for line 2: "))

x = np.linspace(-20, 20, 100)

y1 = m1 * x + c1
y2 = m2 * x + c2

plt.plot(x, y1, label=f"y = {m1}x + {c1}")
plt.plot(x, y2, label=f"y = {m2}x + {c2}")

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.grid(True)

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Dynamic Linear Equation Plotter")

plt.legend()

plt.show()
