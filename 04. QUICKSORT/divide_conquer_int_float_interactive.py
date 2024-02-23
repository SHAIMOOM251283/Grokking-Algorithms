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
    arr = []

    for item in input_str.split():
        try:
            # Try converting the input to an integer
            arr.append(int(item))
        except ValueError:
            try:
                # If conversion to integer fails, try converting to a float
                arr.append(float(item))
            except ValueError:
                # If conversion to float also fails, handle the error
                print("Invalid input:", item, "is neither an integer nor a float.")

    if arr:
        # Find the maximum element using the find_max function
        max_element = find_max(arr)
        # Output the result
        print("Maximum element in the array:", max_element)

if __name__ == "__main__":
    main()
