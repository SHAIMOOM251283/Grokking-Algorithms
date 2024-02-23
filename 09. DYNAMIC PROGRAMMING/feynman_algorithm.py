import numpy as np

def feynman_algorithm(cost_matrix):
    """
    Applies the Feynman algorithm to find the minimum cost path
    through a cost matrix.

    Args:
    - cost_matrix: a 2D numpy array representing the cost matrix

    Returns:
    - min_cost: the minimum cost path
    - path: a list of tuples representing the coordinates of the minimum cost path
    """

    # Initialize a table to store intermediate results and a table to store the path
    n = len(cost_matrix)
    dp = np.zeros_like(cost_matrix)
    path = [[None] * n for _ in range(n)]

    # Initialize the base case
    dp[0][0] = cost_matrix[0][0]

    # Fill the table using dynamic programming
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + cost_matrix[i][0]
        path[i][0] = (i-1, 0)
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + cost_matrix[0][j]
        path[0][j] = (0, j-1)
    for i in range(1, n):
        for j in range(1, n):
            if dp[i-1][j] < dp[i][j-1]:
                dp[i][j] = dp[i-1][j] + cost_matrix[i][j]
                path[i][j] = (i-1, j)
            else:
                dp[i][j] = dp[i][j-1] + cost_matrix[i][j]
                path[i][j] = (i, j-1)

    # Build the path
    min_cost = dp[n-1][n-1]
    min_path = [(n-1, n-1)]
    i, j = n-1, n-1
    while i > 0 or j > 0:
        i, j = path[i][j]
        min_path.append((i, j))
    min_path.reverse()

    # Return the minimum cost and the path
    return min_cost, min_path

# Example usage:
cost_matrix = [
    [1, 3, 5],
    [2, 1, 4],
    [5, 3, 2]
]

min_cost, min_path = feynman_algorithm(cost_matrix)
print("Minimum cost:", min_cost)
print("Minimum cost path:", min_path)
