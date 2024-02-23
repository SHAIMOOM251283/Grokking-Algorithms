import numpy as np

def calculate_euclidean_distance(x1, x2, weights=None):
    # If weights are not provided, use equal weights
    if weights is None:
        weights = np.ones_like(x1)
    # Calculate squared differences with weights
    squared_diff = (x1 - x2) ** 2 * weights
    # Sum up the squared differences
    sum_squared_diff = np.sum(squared_diff)
    # Take the square root of the sum
    result = np.sqrt(sum_squared_diff)
    return result

def main():
    print("Enter the values for array x1 (comma-separated):")
    x1_values = input().strip().split(',')
    x1 = np.array([float(val) for val in x1_values])

    print("Enter the values for array x2 (comma-separated):")
    x2_values = input().strip().split(',')
    x2 = np.array([float(val) for val in x2_values])

    print("Enter the values for array of weights (comma-separated, press Enter for equal weights):")
    weights_input = input().strip()
    if weights_input:
        weights = np.array([float(w) for w in weights_input.split(',')])
    else:
        weights = None

    result = calculate_euclidean_distance(x1, x2, weights)
    print("Result:", result)

if __name__ == "__main__":
    main()
