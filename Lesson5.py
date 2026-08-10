# Create a 7x7 Matrix
import numpy as np
matrix = np.arange(1, 50).reshape(7,7)
print(matrix)

# Extract Middle 3x3 Matrix
import numpy as np
matrix = np.arange(1, 50).reshape(7, 7)
middle = matrix[2:5, 2:5]
print(middle)

# Conditional Selection (Greater than 50)
import numpy as np
arr = np.array([10, 25, 50, 75, 100])
result = arr[arr > 50]
print(result)

# Add Number to every element
import numpy as np
sample_array = np.array([1, 2, 3, 4])
sample_array += 1
print(sample_array)