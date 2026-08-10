# NumPy Function Example

import numpy as np

def solve(x):
    return 2 * x + 3

x = np.array([1, 2, 3, 4, 5])
y = solve(x)
print(y)

# Comprehensive NumPy Program 
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Original Array:", arr)
print("Slice:", arr[1:4])
print("Even Numbers:", arr[arr % 2 == 0])
print("Add 10:", arr + 10)
print("Multiply by 2:", arr * 2)

def square(x):
    return x**2

print("Squared Values:", square(arr))