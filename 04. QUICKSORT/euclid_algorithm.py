def euclid_gcd(a, b):
    # Base case: if b is 0, then the GCD is a
    if b == 0:
        return a
    # Otherwise, recursively call the function with b and the remainder of a divided by b
    return euclid_gcd(b, a % b)

# Example usage:
num1 = 54
num2 = 24
gcd = euclid_gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", gcd)
