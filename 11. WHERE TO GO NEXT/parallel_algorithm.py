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

if __name__ == "__main__":
    # List of numbers
    numbers = [1, 2, 3, 4, 5]

    # Compute squares of numbers in parallel
    squared_numbers = parallel_square(numbers)

    print("Original numbers:", numbers)
    print("Squared numbers:", squared_numbers)
