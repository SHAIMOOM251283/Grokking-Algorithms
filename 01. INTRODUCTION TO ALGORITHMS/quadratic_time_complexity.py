# O(n^2) - Quadratic Time Complexity

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(unsorted_list)
print("Sorted list:", unsorted_list)

# The bubble_sort function has a time complexity of O(n^2) because it has nested loops, and for each element in the outer loop, it compares and swaps elements in the inner loop.