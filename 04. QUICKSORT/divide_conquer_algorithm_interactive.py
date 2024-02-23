def find_max(arr):
    # Base case: if the array has only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursive step: find the maximum element in each half
    max_left = find_max(left_half)
    max_right = find_max(right_half)
    
    # Combine the results: return the maximum of the two maximums
    return max(max_left, max_right)

def main():
    # Prompt the user to input elements of the array separated by spaces
    input_str = input("Enter the elements of the array separated by spaces: ")
    #arr = list(map(int, input_str.split()))
    arr = list(map(float, input_str.split()))

    
    # Find the maximum element using the find_max function
    max_element = find_max(arr)
    
    # Output the result
    print("Maximum element in the array:", max_element)

if __name__ == "__main__":
    main()
