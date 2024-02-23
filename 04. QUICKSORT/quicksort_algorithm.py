def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Example usage:
my_array = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(my_array))  # Output: [1, 1, 2, 3, 6, 8, 10]
