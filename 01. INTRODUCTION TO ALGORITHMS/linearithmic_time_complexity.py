# O(n * log n) - Linearithmic Time Complexity

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage:
unsorted_list = [5, 2, 9, 1, 5, 6]
sorted_list = merge_sort(unsorted_list)
print("Sorted list:", sorted_list)

# The merge_sort function has a time complexity of O(n * log n) because it efficiently divides the input array into smaller parts, sorts them individually, and then merges them back together.