# O(n) - Linear Time Complexity

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
list_to_search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#target_element = 7
target_element = int(input("Enter the number to search for: "))
result = linear_search(list_to_search, target_element)
print("Index of", target_element, "is:", result)

# The linear_search function has a time complexity of O(n) because it iterates through the input list once.