import itertools

class FactorialTimeComplexity:

    def __init__(self):
        self.elements_to_permute = [1, 2, 3]

    def permutation_example(self):
        return list(itertools.permutations(self.elements_to_permute))

    def output(self):
        all_permutations = self.permutation_example()
        print("All permutations:", all_permutations)

if __name__ == '__main__':
    timeComplexity = FactorialTimeComplexity()
    timeComplexity.output()
    
# The time complexity of this operation is O(n!) because it explores all possible arrangements of the input elements.
# O(n!) - Factorial Time Complexity