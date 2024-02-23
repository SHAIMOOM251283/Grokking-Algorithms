from functools import reduce
from concurrent.futures import ProcessPoolExecutor
# from concurrent.futures import ThreadPoolExecutor  # You can also use ThreadPoolExecutor for threads

def add(x, y):
    return x + y

def parallel_add(arr1, arr2):
    # Distribute the addition work across processes using map
    with ProcessPoolExecutor() as executor:  # Use ThreadPoolExecutor for threads
        result = executor.map(add, arr1, arr2)
    
    # Use reduce to combine the results
    total_sum = reduce(add, result)
    return total_sum

if __name__ == "__main__":
    # List of numbers
    arr1 = [1, 2, 3, 4, 5]
    arr2 = map(lambda x: 2 * x, arr1)  # arr2 = [2, 4, 6, 8, 10]

    # Perform the distributed addition
    result = parallel_add(arr1, arr2)

    print("Result of parallel addition:", result)
