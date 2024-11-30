class QuadraticTimeComplexity:

    def __init__(self):
        self.unsorted_list = [64, 34, 25, 12, 22, 11, 90]

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def run(self):
        print("Unsorted list:", self.unsorted_list)
        self.bubble_sort(self.unsorted_list)
        print("Sorted list:", self.unsorted_list)

if __name__ == '__main__':
    qtc = QuadraticTimeComplexity()
    qtc.run()