def get_user_input():
    try:
        elements = list(map(int, input("Enter the elements separated by space: ").split()))
        return elements
    except ValueError:
        print("Error: Please enter valid integers separated by space.")
        return get_user_input()

def access_and_modify_elements(my_array):
    try:
        first_element = my_array[0]  
        second_element = my_array[1]  
        print("First Element:", first_element)
        print("Second Element:", second_element)

        # Modify the third element
        my_array[2] = 10
        print("Array after modifying the third element:", my_array)

        # Length of the array
        array_length = len(my_array)  
        print("Length of the Array:", array_length)

    except IndexError:
        print("Error: Array index out of range.")

# Main program
user_input = get_user_input()
access_and_modify_elements(user_input)
