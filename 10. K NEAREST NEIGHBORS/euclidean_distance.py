import numpy as np

# Define the arrays
x1 = np.array([3, 4, 4, 1, 4])
x2 = np.array([4, 3, 5, 1, 5])

# Calculate squared differences
squared_diff = (x1 - x2) ** 2

# Sum up the squared differences
sum_squared_diff = np.sum(squared_diff)

# Take the square root of the sum
result = np.sqrt(sum_squared_diff)

print("Result:", result)
