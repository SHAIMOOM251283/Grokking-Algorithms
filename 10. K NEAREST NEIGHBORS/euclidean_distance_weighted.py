import numpy as np

# Define the arrays
x1 = np.array([3, 4, 4, 1, 4])
x2 = np.array([4, 3, 5, 1, 5])

# Define weights
weights = np.array([1, 1, 1, 1, 1])  # Weights for each feature, e.g., each movie category

# Apply weights to squared differences
weighted_squared_diff = (x1 - x2) ** 2 * weights

# Sum up the weighted squared differences
sum_weighted_squared_diff = np.sum(weighted_squared_diff)

# Take the square root of the sum
result = np.sqrt(sum_weighted_squared_diff)

print("Result:", result)
