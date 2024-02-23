import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]
    return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
print("Original array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)

