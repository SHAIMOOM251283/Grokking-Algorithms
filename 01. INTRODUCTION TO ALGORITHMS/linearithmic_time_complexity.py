class LinearithmicTimeComplexity:

    def __init__(self):
        unsorted_list = [5, 2, 9, 1, 5, 6]
        self.sorted_list = self.merge_sort(unsorted_list)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def run(self):
        print("Unsorted list:", [5, 2, 9, 1, 5, 6])
        sorted_list = self.sorted_list
        print("Sorted list:", sorted_list)

if __name__ == '__main__':
    ltc = LinearithmicTimeComplexity()
    ltc.run()