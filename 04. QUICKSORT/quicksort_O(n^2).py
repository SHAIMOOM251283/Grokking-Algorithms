def quicksort_worst_case(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]
    return quicksort_worst_case(less_than_pivot) + [pivot] + quicksort_worst_case(greater_than_pivot)

# Example usage
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Original array:", arr)
sorted_arr = quicksort_worst_case(arr)
print("Sorted array:", sorted_arr)
