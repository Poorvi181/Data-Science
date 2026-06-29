import numpy as np

#create a 3D array

arr = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(arr)

print(arr.shape)

print(arr.ndim)

print(arr.size)

print(arr.dtype)

arr = np.arange(24).reshape(2, 3, 4)
print(arr)

arr = np.zeroes((2, 3, 4))
print(arr)

arr = np.ones((2, 3, 4))
print(arr)

arr = np.full((2, 4, 5), 10)
print(arr)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0][1][2])

print(arr[1][1][2])
print(arr.nbytes)

print(arr[0, :, :])

print(arr[1, :, :])

print(arr[:, 0, :])

print(arr[:, 1, :])

print(arr[:, :, 0])

print(arr[:, :, 1])

print(arr[:, :, 2])



