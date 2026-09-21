import numpy as np

matrix = np.arange(196).reshape(14, 14)

middle = matrix[3:10, 3:10]
first_row = matrix[0, :]
last_column = matrix[:, -1]

print("14 x 14 Matrix:")
print(matrix)

print("Middle 7 x 7 Matrix:")
print(middle)

print("First Row:")
print(first_row)

print("Last Column:")
print(last_column)