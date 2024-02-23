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
    
    # Convert input strings to integers
    my_array = [int(num) for num in array_input]
    
    sorted_array = quicksort(my_array)
    print("Sorted array:", sorted_array)

if __name__ == "__main__":
    main()
