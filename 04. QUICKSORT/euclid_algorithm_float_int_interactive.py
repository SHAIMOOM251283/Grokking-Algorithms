def euclid_gcd(a, b):
    # Base case: if b is 0, then the GCD is a
    if b == 0:
        return a
    # Otherwise, recursively call the function with b and the remainder of a divided by b
    return euclid_gcd(b, a % b)

def main():
    # Prompt the user to input two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    # Convert the numbers to integers for GCD calculation
    num1_int = int(num1)
    num2_int = int(num2)

    # Calculate the GCD using Euclid's algorithm
    gcd = euclid_gcd(num1_int, num2_int)
    print("The GCD of", num1, "and", num2, "is:", gcd)

if __name__ == "__main__":
    main()
