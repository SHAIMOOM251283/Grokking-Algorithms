import numpy as np

def simplex(c, A, b):
    m, n = A.shape
    c = np.array(c, dtype=float)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    # Add slack variables to convert inequalities to equalities
    slack_vars = np.eye(m)
    A = np.hstack((A, slack_vars))
    c = np.concatenate((c, np.zeros(m)))

    # Create initial tableau
    tableau = np.vstack((np.hstack((np.array([0]), -c, np.zeros(m))),
                         np.hstack((b.reshape(-1, 1), A, np.eye(m)))))

    while np.any(tableau[0, 1:] < 0):
        # Select entering variable (most negative coefficient in the objective function)
        entering_idx = np.argmin(tableau[0, 1:])
        entering_var = tableau[:, entering_idx+1]

        # Select leaving variable (minimum ratio test)
        leaving_idx = np.argmin(tableau[1:, 0] / entering_var[1:])
        leaving_idx += 1  # Account for the extra row in tableau
        leaving_var = tableau[leaving_idx, :]

        # Pivot
        tableau[leaving_idx, :] /= leaving_var[entering_idx + 1]
        for i in range(tableau.shape[0]):
            if i != leaving_idx:
                tableau[i, :] -= tableau[i, entering_idx+1] * tableau[leaving_idx, :]

    # Extract solution
    solution = dict()
    for i in range(1, n + 1):
        if i in tableau[0, 1:]:
            idx = np.where(tableau[0, 1:] == i)[0][0]
            solution[f'x{i}'] = tableau[idx+1, 0]
        else:
            solution[f'x{i}'] = 0

    return solution, -tableau[0, 0]  # Maximize the negative objective function

# Example usage:
c = [-2, -3]  # Coefficients of the objective function to maximize: -2x1 - 3x2
A = np.array([[1, 1],  # Coefficients of the constraints
              [2, 1]])
b = np.array([4, 5])    # Right-hand side of the constraints

solution, optimal_value = simplex(c, A, b)
print("Solution:", solution)
print("Optimal value:", optimal_value)
