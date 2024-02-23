def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

def main():
    # Prompt the user to input numbers separated by spaces
    input_str = input("Enter the numbers separated by spaces: ")

    # Convert input string to a list of numbers (both integers and floats)
    arr = []
    for num in input_str.split():
        try:
            arr.append(int(num))
        except ValueError:
            try:
                arr.append(float(num))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                return

    # Calculate the sum of the numbers
    total = sum(arr)
    
    # Output the sum
    print("Sum of the numbers:", total)

if __name__ == "__main__":
    main()
