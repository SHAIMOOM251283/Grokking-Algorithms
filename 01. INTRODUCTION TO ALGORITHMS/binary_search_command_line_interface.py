def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2  # Use integer division to avoid float
        guess = my_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

# Take user input for the list
try:
    input_list = input("Enter a sorted list of numbers separated by spaces: ")
    my_list = [int(x) for x in input_list.split()]
    my_list.sort()  # Ensure the list is sorted for binary search
except ValueError:
    print("Invalid input. Please enter a valid sorted list of numbers.")
    exit()

# Perform binary search
search_item = int(input("Enter the number to search for: "))
result = binary_search(my_list, search_item)

# Display result
if result is not None:
    print(f"{search_item} found at index {result}.")
else:
    print(f"{search_item} not found in the list.")
