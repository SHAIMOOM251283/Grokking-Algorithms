# Create an empty dictionary
book = {}

# Add items and their prices to the dictionary
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

# Print the dictionary
print(book)

print(book["avocado"])

# A hash table maps keys to values.

# Accessing an item from a dictionary by its key has an average time complexity of O(1). 
# This means that regardless of the size of the dictionary, the time it takes to access a specific item remains constant on average. 
# This efficiency is achieved through the use of hash tables, which allow for direct lookup of values based on their keys. 
# Therefore, accessing an item by its key in a dictionary is considered a constant-time operation, making it O(1) in terms of time complexity.
