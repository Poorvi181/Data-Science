# Array Slicing

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

slice_arr = arr[0:4]

print("Original Array: \n", arr)
print("Sliced Array: \n", slice_arr)

# 2D ARRAY SLICING

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr[0:2, 1:3])


# 3D Array Slicing Example 
import numpy as np

arr = np.array(
    [
        [
            [1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9],
        ],
         [
             
            [10, 11, 12], 
            [13, 14, 15],
            [16, 17, 18]
        ]
    ]
)

print("Original 3D Array:")
print(arr)

# Slice the first layer, first two rows, first two columns
result = arr[0, 0:2, 0:2]

print("\nSliced Array:")
print(result)