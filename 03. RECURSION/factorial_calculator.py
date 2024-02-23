def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        result = n * factorial(n - 1)
        return result

# Take user input for the number
user_input = int(input("Enter a non-negative integer to calculate its factorial: "))

# Check if the input is a non-negative integer
if user_input < 0:
    print("Please enter a non-negative integer.")
else:
    # Calculate and display the factorial
    result = factorial(user_input)
    print(f"The factorial of {user_input} is:", result)

# n!=n×(n−1)×(n−2)×…×3×2×1

# The factorial of 5 is: 120
# 5!=5×4×3×2×1=1205!=5×4×3×2×1=120
# So, the factorial of 5 is the product of all positive integers from 5 down to 1.

# The factorial of 7 is: 5040
# 7!=7×6×5×4×3×2×1=50407!=7×6×5×4×3×2×1=5040
# Similarly, the factorial of 7 is the product of all positive integers from 7 down to 1.