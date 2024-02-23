# Homogeneous Array (Integer)
size = int(input("Enter the size of the array: "))
integer_array = []

for i in range(size):
    user_input = int(input(f"Enter integer for index {i}: "))
    integer_array.append(user_input)

# Accessing elements
print("Array:", integer_array)
