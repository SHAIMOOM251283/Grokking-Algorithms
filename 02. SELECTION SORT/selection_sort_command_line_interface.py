def findSmallest(arr):
    smallest = arr[0]  # Stores the smallest value
    smallest_index = 0  # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

# Input from the user
try:
    input_list = input("Enter a list of numbers separated by spaces: ")
    input_list = [int(x) for x in input_list.split()]
except ValueError:
    print("Invalid input. Please enter a valid list of numbers.")
    exit()

# Sort and print the sorted list
sorted_list = selectionSort(input_list)
print("Sorted Array:", sorted_list)
