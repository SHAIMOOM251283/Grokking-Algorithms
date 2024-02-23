# Taking input from the user for the list of elements
my_array = list(map(int, input("Enter the elements separated by space: ").split()))

print("Current Array:", my_array)

# Accessing elements
index = int(input("Enter the index to access: "))
print("Element at index", index, "is:", my_array[index])

# Modifying elements
index = int(input("Enter the index to modify: "))
new_value = int(input("Enter the new value: "))
my_array[index] = new_value
print("Array after modifying the element at index", index, ":", my_array)

# Length of the array
array_length = len(my_array)  
print("Length of the Array:", array_length)

