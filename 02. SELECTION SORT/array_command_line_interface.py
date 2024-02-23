# Taking input from the user for the list of elements
my_array = list(map(int, input("Enter the elements separated by space: ").split()))

# Accessing and modifying elements using a loop
while True:
    print("Current Array:", my_array)
    
    # Taking user choice
    choice = input("Do you want to access or modify elements? (Type 'access', 'modify', or 'exit'): ").lower()

    if choice == 'access':
        # Accessing elements
        index = int(input("Enter the index to access: "))
        if 0 <= index < len(my_array):
            print("Element at index", index, "is:", my_array[index])
        else:
            print("Invalid index. Please enter a valid index.")

    elif choice == 'modify':
        # Modifying elements
        index = int(input("Enter the index to modify: "))
        if 0 <= index < len(my_array):
            new_value = int(input("Enter the new value: "))
            my_array[index] = new_value
            print("Array after modifying the element at index", index, ":", my_array)
        else:
            print("Invalid index. Please enter a valid index.")

    elif choice == 'exit':
        break

    else:
        print("Invalid choice. Please enter 'access', 'modify', or 'exit'.")

# Length of the array
array_length = len(my_array)  
print("Length of the Array:", array_length)
