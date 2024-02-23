# O(n!) - Factorial Time Complexity

import itertools

def permutation_example(elements):
    return list(itertools.permutations(elements))

# Example usage:
elements_to_permute = [1, 2, 3]
all_permutations = permutation_example(elements_to_permute)
print("All permutations:", all_permutations)

# The time complexity of this operation is O(n!) because it explores all possible arrangements of the input elements.
