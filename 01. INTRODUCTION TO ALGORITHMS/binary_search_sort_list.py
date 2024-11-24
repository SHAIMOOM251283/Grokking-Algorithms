class BinarySearchwithSort:

    def __init__(self):
        self.list = input("Enter a sorted list of numbers separated by spaces: ")
        self.my_list = [int(x) for x in self.list.split()]
        print(self.my_list)
        self.my_list.sort()
        print(self.my_list)
        self.search_item = int(input("Enter the number to search for: "))

    def binary_search(self):
        low = 0
        high = len(self.my_list) - 1

        while low <= high:
            mid = (low + high) // 2  # Use integer division to avoid float
            guess = self.my_list[mid]
            if guess == self.search_item:
                return mid
            if guess > self.search_item:
                high = mid - 1
            else:
                low = mid + 1
        return None

    def output(self):
        result = self.binary_search()
        if result is not None:
            print(f"{self.search_item} found at index {result}.")
        else:
            print(f"{self.search_item} not found in the list.")

if __name__ == '__main__':
    SortSearch = BinarySearchwithSort()
    SortSearch.output()