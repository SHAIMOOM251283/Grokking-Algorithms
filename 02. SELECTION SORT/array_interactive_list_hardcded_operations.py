# Taking input from the user for the list of elements
my_array = list(map(int, input("Enter the elements separated by space: ").split()))

# Accessing elements using indices
first_element = my_array[0]  
second_element = my_array[1]  
print("First Element:", first_element)
print("Second Element:", second_element)

# Modifying elements
my_array[2] = 10
print("Array after modifying the third element:", my_array)

# Length of the array
array_length = len(my_array)  
print("Length of the Array:", array_length)
