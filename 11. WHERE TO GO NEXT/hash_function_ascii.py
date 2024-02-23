def simple_hash(string, table_size):
    """
    A simple hash function that takes a string and gives back the slot number for that string.
    
    Args:
    - string: The string to be hashed.
    - table_size: The size of the hash table.
    
    Returns:
    - slot_number: The slot number for the given string.
    """
    hash_value = 0
    for char in string:
        hash_value += ord(char)  # Using the ASCII value of characters for simplicity
    slot_number = hash_value % table_size
    return slot_number

# Example usage:
hash_table_size = 10
string_to_hash = "hello"
slot_number = simple_hash(string_to_hash, hash_table_size)
print(f"The slot number for '{string_to_hash}' is: {slot_number}")

# ASCII stands for American Standard Code for Information Interchange. 

#     Calculate Hash Value:
#        The ASCII values of the characters in the string "hello" are as follows:
#            'h': 104
#            'e': 101
#            'l': 108 (twice)
#            'o': 111
#        The sum of these ASCII values is: 104 + 101 + 108 + 108 + 111 = 532

#    Modulus Operation:
#        The calculated hash value (532) is then taken modulo the hash table size (10):
#            532 % 10 = 2