def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

# Example: Calculate and print the factorial of 5
#result = fact(3)
#print("The factorial of 3 is:", result)

# Take user input for the number
user_input = int(input("Enter a non-negative integer to calculate its factorial: "))

# Check if the input is a non-negative integer
if user_input < 1:
    print("Please enter a non-negative integer.")
else:
    # Calculate and display the factorial
    result = fact(user_input)
    print(f"The factorial of {user_input} is:", result)