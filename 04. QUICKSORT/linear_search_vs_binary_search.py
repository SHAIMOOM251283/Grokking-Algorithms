def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 15
print("Linear search result:", linear_search(my_list, target))
print("Binary search result:", binary_search(my_list, target))
