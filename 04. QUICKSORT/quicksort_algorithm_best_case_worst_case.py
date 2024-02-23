def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

# Test the algorithm
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)

# Worst case: already sorted in ascending or descending order
print("Worst case:")
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

# Best case: array randomly ordered
import random
random.shuffle(arr)
print("\nBest case:")
quicksort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
