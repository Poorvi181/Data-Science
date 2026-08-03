import numpy as np

array1 = np.zeros((4, 5))
array2 = np.ones((3, 3))
array3 = np.arange(20).reshape(4, 5)

arrays = [array1, array2, array3]

for i, arr in enumerate(arrays, start=1):
    print(f"\nArray {i}:")
    print(arr)
    print("Number of dimensions:", arr.ndim)
    print("Shape:", arr.shape)
    print("Total elements:", arr.size)
    print("Memory usage:", arr.nbytes, "bytes")