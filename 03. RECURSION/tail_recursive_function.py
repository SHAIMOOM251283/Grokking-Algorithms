def factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return factorial(n - 1, accumulator * n)

# Take user input for the number
user_input = int(input("Enter a non-negative integer to calculate its factorial: "))

# Check if the input is a non-negative integer
if user_input < 0:
    print("Please enter a non-negative integer.")
else:
    # Calculate and display the factorial
    result = factorial(user_input)
    print(f"The factorial of {user_input} is:", result)