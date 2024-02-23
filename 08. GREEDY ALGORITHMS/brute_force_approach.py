import time
import itertools

def subset_sum(numbers, target):
    # Generate all possible subsets of the numbers
    subsets = itertools.chain.from_iterable(itertools.combinations(numbers, r) for r in range(len(numbers)+1))
    
    # Check if any subset sums up to the target
    for subset in subsets:
        if sum(subset) == target:
            return True
    return False

# Example set of numbers and target sum
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 25

# Measure computation time for increasing problem sizes
for n in range(1, len(numbers)+1):
    start_time = time.time()
    found = subset_sum(numbers[:n], target_sum)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Problem size: {n}, Found subset sum: {found}, Computation time: {elapsed_time:.6f} seconds")

# This code generates subsets of increasing sizes from the given set of numbers and checks each subset to see if its sum equals the target sum. 
# As the problem size increases, the number of subsets grows exponentially, leading to longer computation times. 
# This demonstrates the difficulty of solving NP-complete problems using brute-force approaches, 
# as the computation time becomes impractical for larger problem instances.