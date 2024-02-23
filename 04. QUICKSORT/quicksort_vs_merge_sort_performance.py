import time
import random

# Quicksort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choosing the pivot (middle element)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Merge Sort implementation
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
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

# Test the sorting algorithms
arr = random.sample(range(1, 100000), 10000)  # Generating a random array of size 10000
start_time = time.time()
sorted_arr_quick = quicksort(arr)
end_time = time.time()
print("Quicksort time:", end_time - start_time, "seconds")  # Time taken by Quicksort

start_time = time.time()
sorted_arr_merge = merge_sort(arr)
end_time = time.time()
print("Merge Sort time:", end_time - start_time, "seconds")  # Time taken by Merge Sort
