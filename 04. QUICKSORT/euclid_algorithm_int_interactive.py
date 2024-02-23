def euclid_gcd(a, b):
    # Base case: if b is 0, then the GCD is a
    if b == 0:
        return a
    # Otherwise, recursively call the function with b and the remainder of a divided by b
    return euclid_gcd(b, a % b)

def main():
    # Prompt the user to input two integers
    try:
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    # Calculate the GCD using Euclid's algorithm
    gcd = euclid_gcd(num1, num2)
    print("The GCD of", num1, "and", num2, "is:", gcd)

if __name__ == "__main__":
    main()
