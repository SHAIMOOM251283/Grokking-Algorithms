# O(log n) - Logarithmic Time Complexity

import math

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#target_element = 7
target_element = int(input("Enter the number to search for: "))
result = binary_search(sorted_list, target_element)
print("Index of", target_element, "is:", result)

# The binary_search function has a time complexity of O(log n) because it efficiently halves the search space at each step.