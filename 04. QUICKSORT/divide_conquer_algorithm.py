def find_max(arr):
    # Base case: if the array has only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursive step: find the maximum element in each half
    max_left = find_max(left_half)
    max_right = find_max(right_half)
    
    # Combine the results: return the maximum of the two maximums
    return max(max_left, max_right)

# Example usage:
arr = [3, 7, 2, 9, 5, 1, 8, 6]
print("Maximum element in the array:", find_max(arr))
