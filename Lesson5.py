# Create a 7x7 Matrix
import numpy as np
matrix = np.arrange(1, 50).reshape(7,7)
print(matrix)

# Extract Middle 3x3 Matrix
import numpy as np
matrix = np.arrange(1, 50).reshape(7, 7)
middle = matrix[2:5, 2:5]
print(middle)

# Conditional