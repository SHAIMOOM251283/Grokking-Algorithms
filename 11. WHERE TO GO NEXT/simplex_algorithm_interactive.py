import numpy as np

def simplex(c, A, b):
    """
    Simplex algorithm implementation to solve linear programming problems.

    Args:
    c: 1-D numpy array of coefficients of the objective function to be maximized
    A: 2-D numpy array representing the coefficients of the constraints
    b: 1-D numpy array representing the right-hand side values of the constraints

    Returns:
    Optimal solution and the optimal value of the objective function
    """
    m, n = A.shape
    c = c.astype(float)
    A = A.astype(float)
    b = b.astype(float)

    # Add slack variables to convert inequality constraints to equality constraints
    A = np.hstack((A, np.eye(m)))
    c = np.concatenate((c, np.zeros(m)))

    # Initial tableau
    tableau = np.vstack((np.hstack((np.array([0]), -c, np.array([1]))),
                         np.hstack((b.reshape(-1, 1), A, np.zeros((m, 1))))))

    while np.any(tableau[0, 1:] < 0):
        # Select entering variable (most negative coefficient in objective function)
        entering = np.argmin(tableau[0, 1:])+1

        # Select leaving variable (minimum ratio test)
        ratios = tableau[1:, 0] / tableau[1:, entering]
        leaving = np.argmin(ratios) + 1

        # Pivot
        pivot = tableau[leaving, entering]
        tableau[leaving, :] /= pivot
        for i in range(tableau.shape[0]):
            if i != leaving:
                tableau[i, :] -= tableau[i, entering] * tableau[leaving, :]

    optimal_solution = tableau[0, -1]
    return tableau[1:, -1], optimal_solution

def main():
    # Take user input for the number of decision variables and constraints
    num_variables = int(input("Enter the number of decision variables: "))
    num_constraints = int(input("Enter the number of constraints: "))

    # Take user input for the coefficients of the objective function
    objective_coefficients = []
    print("Enter the coefficients of the objective function:")
    for i in range(num_variables):
        coefficient = float(input(f"Enter coefficient for x{i+1}: "))
        objective_coefficients.append(coefficient)

    # Take user input for the coefficients of the constraints
    constraint_coefficients = []
    constraints_rhs = []
    print("Enter the coefficients of the constraints (one constraint at a time):")
    for i in range(num_constraints):
        constraint_coefficient = []
        print(f"Constraint {i+1}:")
        for j in range(num_variables):
            coefficient = float(input(f"Enter coefficient for x{j+1}: "))
            constraint_coefficient.append(coefficient)
        constraint_rhs = float(input("Enter the RHS value of the constraint: "))
        constraint_coefficients.append(constraint_coefficient)
        constraints_rhs.append(constraint_rhs)

    # Solve the linear programming problem
    c = np.array(objective_coefficients)
    A = np.array(constraint_coefficients)
    b = np.array(constraints_rhs)
    solution, optimal_value = simplex(c, A, b)

    # Print the solution
    print("\nOptimal Solution:")
    for i, sol in enumerate(solution):
        print(f"x{i+1} = {sol}")

    print("\nOptimal Value of the Objective Function:", optimal_value)

if __name__ == "__main__":
    main()
