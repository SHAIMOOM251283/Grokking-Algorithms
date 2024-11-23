class BinarySearch:

    def __init__(self):
        self.my_list = [1, 3, 5, 7, 9]
        self.item = int(input("Enter Value: "))

    def binary_search(self):
        low = 0
        high = len(self.my_list) - 1

        while low <= high:
            mid = (low + high) // 2  # Use integer division to avoid float
            guess = self.my_list[mid]
            if guess == self.item:
                return mid
            if guess > self.item:
                high = mid - 1
            else:
                low = mid + 1
        return None

    def output(self):
        result = self.binary_search()
        if result is not None:
            print(f"Item found at index {result}")
        else:
            print("Item not found in the list.")
        
if __name__ == '__main__': 
    while True:
        search = BinarySearch()
        search.output()

        repeat = input("Do you want to enter another value (enter 'yes' or 'no'): ")
        if repeat != 'yes':
            break