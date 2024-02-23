import multiprocessing

def square(n):
    """Function to compute square of a number."""
    return n * n

def parallel_square(numbers):
    """Function to compute squares of numbers in parallel."""
    # Create a pool of processes
    pool = multiprocessing.Pool()

    # Map the square function to the list of numbers using multiple processes
    results = pool.map(square, numbers)

    # Close the pool to release resources
    pool.close()
    pool.join()

    return results

def main():
    # Prompt the user to enter a list of numbers separated by spaces
    numbers_input = input("Enter a list of numbers separated by spaces: ")

    # Convert the input string into a list of integers
    numbers = [int(num) for num in numbers_input.split()]

    # Compute squares of numbers in parallel
    squared_numbers = parallel_square(numbers)

    print("Original numbers:", numbers)
    print("Squared numbers:", squared_numbers)

if __name__ == "__main__":
    main()
