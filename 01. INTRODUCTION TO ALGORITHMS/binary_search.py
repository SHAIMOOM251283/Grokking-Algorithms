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
    return None  # Move this line outside the while loop

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))

print(binary_search(my_list, -1))

# It's generally a good practice to avoid using names that are already built-in Python types or functions (like list) to prevent confusion and potential errors. 
# It's better to use a different name to avoid shadowing built-in names and make your code more readable.