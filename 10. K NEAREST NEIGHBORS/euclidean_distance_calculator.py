import numpy as np

def calculate_euclidean_distance(x1, x2):
    # Calculate squared differences
    squared_diff = (x1 - x2) ** 2
    # Sum up the squared differences
    sum_squared_diff = np.sum(squared_diff)
    # Take the square root of the sum
    result = np.sqrt(sum_squared_diff)
    return result

def main():
    print("Enter the values for array x1 (comma-separated):")
    x1_values = input().strip().split(',')
    x1 = np.array([int(val) for val in x1_values])

    print("Enter the values for array x2 (comma-separated):")
    x2_values = input().strip().split(',')
    x2 = np.array([int(val) for val in x2_values])

    result = calculate_euclidean_distance(x1, x2)
    print("Result:", result)

if __name__ == "__main__":
    main()
