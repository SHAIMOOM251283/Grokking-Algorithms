def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def main():
    print("Welcome to QuickSort!")
    print("Enter the elements of the array separated by spaces:")
    array_input = input().strip().split()
    
    # Convert input strings to floats, handling potential errors
    my_array = []
    for num in array_input:
        try:
            my_array.append(float(num))
        except ValueError:
            print(f"Invalid input: '{num}' is not a number. Please enter numbers only.")
            return
    
    print("Enter the value of the pivot:")
    pivot_value = input().strip()

    # Ensure the pivot value is in the array
    if pivot_value not in array_input:
        print("Pivot value is not in the array. Please choose a value from the array.")
        return
    
    # Move pivot to the front of the array
    pivot_index = array_input.index(pivot_value)
    my_array[0], my_array[pivot_index] = my_array[pivot_index], my_array[0]

    sorted_array = quicksort(my_array)
    print("Sorted array:", sorted_array)

if __name__ == "__main__":
    main()
