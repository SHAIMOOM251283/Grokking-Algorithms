def count_items_recursive(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: return 1 (for the current item) plus the count of the remaining items in the list
    return 1 + count_items_recursive(lst[1:])

def main():
    # Prompt the user to input items of the list separated by spaces
    input_str = input("Enter the items of the list separated by spaces: ")

    # Convert input string to a list of items
    lst = input_str.split()

    # Count the number of items in the list using the recursive function
    count = count_items_recursive(lst)

    # Output the result
    print("Number of items in the list:", count)

if __name__ == "__main__":
    main()
