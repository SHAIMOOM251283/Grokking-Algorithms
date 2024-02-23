from functools import reduce
from concurrent.futures import ThreadPoolExecutor

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Function to calculate the sum of a list
def sum_list(nums):
    return sum(nums)

# Distributed sum calculation function
def distributed_sum(numbers, chunk_size=2):
    # Divide the list into chunks
    chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
    
    # Function to calculate sum of each chunk
    def sum_chunk(chunk):
        return sum_list(chunk)
    
    # Use ThreadPoolExecutor for parallel execution
    with ThreadPoolExecutor(max_workers=len(chunks)) as executor:
        # Map each chunk to sum_chunk function
        chunk_sums = executor.map(sum_chunk, chunks)
        
        # Use reduce to combine the results
        total_sum = reduce(lambda x, y: x + y, chunk_sums)
    
    return total_sum

# Calculate distributed sum
result = distributed_sum(numbers, chunk_size=3)
print("Distributed sum:", result)
