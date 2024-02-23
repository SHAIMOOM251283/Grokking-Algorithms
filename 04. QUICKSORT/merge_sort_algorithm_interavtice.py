def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Compare elements from both lists and merge them
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Add remaining elements from the left or right list
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

def main():
    # Prompt the user to input elements of the array separated by spaces
    input_str = input("Enter the elements of the array separated by spaces: ")

    # Convert input string to a list of numbers (both integers and floats)
    arr = []
    for num in input_str.split():
        try:
            arr.append(int(num))
        except ValueError:
            try:
                arr.append(float(num))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                return

    # Perform merge sort on the array
    sorted_arr = merge_sort(arr)
    
    # Output the sorted array
    print("Sorted array:", end=" ")
    for num in sorted_arr:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    main()
