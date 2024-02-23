import numpy as np

def calculate_euclidean_distance():
    print("Enter the ratings for User 1:")
    x1 = np.array([float(input(f"Rating for feature {i + 1}: ")) for i in range(5)])

    print("Enter the ratings for User 2:")
    x2 = np.array([float(input(f"Rating for feature {i + 1}: ")) for i in range(5)])

    print("Enter the weights for each feature (press Enter for default weights [1, 1, 1, 1, 1]):")
    weights_input = input("Weights (comma-separated): ").strip()
    if weights_input:
        weights = np.array([float(w) for w in weights_input.split(',')])
    else:
        weights = np.ones(5)  # Default weights

    # Apply weights to squared differences
    weighted_squared_diff = (x1 - x2) ** 2 * weights

    # Sum up the weighted squared differences
    sum_weighted_squared_diff = np.sum(weighted_squared_diff)

    # Take the square root of the sum
    result = np.sqrt(sum_weighted_squared_diff)

    print("\nEuclidean distance:", result)

if __name__ == "__main__":
    calculate_euclidean_distance()
