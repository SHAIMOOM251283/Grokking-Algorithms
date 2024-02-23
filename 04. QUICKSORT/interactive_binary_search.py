def binary_search(array, target):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def main():
    array = input("Enter sorted array elements separated by spaces: ").split()
    target = input("Enter the element to search for: ")
    
    index = binary_search(array, target)
    if index != -1:
        print(f"Element found at index {index}.")
    else:
        print("Element not found.")

if __name__ == "__main__":
    main()
