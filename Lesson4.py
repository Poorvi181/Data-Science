# Array Slicing

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

slice_arr = arr[0:4]

print("Original Array: \n", arr)
print("Sliced Array: \n", slice_arr)

# 2D ARRAY SLICING

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr[0:2, 1:3])