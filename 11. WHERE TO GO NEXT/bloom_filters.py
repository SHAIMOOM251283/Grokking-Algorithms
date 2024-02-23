import math
import mmh3 

class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.hash_functions = hash_functions
        self.bit_array = [False] * size

    def add(self, item):
        for i in range(self.hash_functions):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = True

    def contains(self, item):
        for i in range(self.hash_functions):
            index = mmh3.hash(item, i) % self.size
            if not self.bit_array[index]:
                return False
        return True

# Example usage:
bloom_filter = BloomFilter(size=10, hash_functions=3)

# Add some items
bloom_filter.add("apple")
bloom_filter.add("banana")
bloom_filter.add("orange")

# Check for membership
print(bloom_filter.contains("apple"))  # Output: True
print(bloom_filter.contains("banana")) # Output: True
print(bloom_filter.contains("grape"))  # Output: False (False positive possible)
