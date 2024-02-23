import random
import timeit

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Merge the two lists while preserving order
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Add any remaining elements
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

# Generate a random list of integers
arr = [random.randint(0, 1000) for _ in range(1000)]

# Measure the time taken by quicksort
quicksort_time = timeit.timeit(lambda: quicksort(arr), number=1)
print("Time taken by quicksort:", quicksort_time)

# Measure the time taken by merge sort
merge_sort_time = timeit.timeit(lambda: merge_sort(arr), number=1)
print("Time taken by merge sort:", merge_sort_time)
