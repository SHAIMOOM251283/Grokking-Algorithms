import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def test_quicksort():
    # Best-case scenario: already sorted array
    arr_best_case = list(range(10000))
    start_time = time.time()
    sorted_arr_best_case = quicksort(arr_best_case)
    end_time = time.time()
    print("Best-case scenario time:", end_time - start_time)

    # Worst-case scenario: reversed sorted array
    arr_worst_case = list(range(10000, 0, -1))
    start_time = time.time()
    sorted_arr_worst_case = quicksort(arr_worst_case)
    end_time = time.time()
    print("Worst-case scenario time:", end_time - start_time)

if __name__ == "__main__":
    test_quicksort()
