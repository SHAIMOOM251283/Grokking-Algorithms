class LinearTimeComplexity:

    def __init__(self):
        self.list_to_search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.target_element = int(input("Enter the number to search for: "))

    def linear_search(self):
        for i in range(len(self.list_to_search)):
            if self.list_to_search[i] == self.target_element:
                return i
        return -1

    def output(self):
        result = self.linear_search()
        if result != -1:
            print(f"Index of {self.target_element} is: {result}")
        else:
            print(f"{self.target_element} is not in the list.")
        
if __name__ == '__main__':
    search = LinearTimeComplexity()
    search.output()

# The linear_search function has a time complexity of O(n) because it iterates through the input list once.
# O(n) - Linear Time Complexity
