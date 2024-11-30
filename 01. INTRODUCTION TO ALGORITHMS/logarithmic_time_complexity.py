class LogarithmicTimeComplexity:

    def __init__(self):
        # Initializing sorted_list with a default sorted list
        self.sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Taking user input for target element
        self.target_element = int(input("Enter the number to search for: "))
        # Initialize arr as None (you can still modify it later if needed)
        self.arr = None

    def binary_search(self):
        # Use self.sorted_list for searching
        arr = self.sorted_list  # No need to pass arr as a parameter
        
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == self.target_element:
                return mid
            elif arr[mid] < self.target_element:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def run(self):
        # Here we are calling the binary_search method without arguments
        result = self.binary_search()  # No need to pass arr explicitly
        if result != -1:
            print(f"Index of {self.target_element} is: {result}")
        else:
            print(f"{self.target_element} is not in the list.")

if __name__ == '__main__':
    ltc = LogarithmicTimeComplexity()
    ltc.run()
