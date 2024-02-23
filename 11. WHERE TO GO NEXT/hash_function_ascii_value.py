def simple_hash(string, table_size):
    """
    A simple hash function that takes a string and a table size
    and returns the slot number for that string.
    """
    hash_value = 0
    for char in string:
        hash_value += ord(char)  # Sum up the ASCII values of characters
    return hash_value % table_size  # Modulus to fit within table size


# Example usage:
table_size = 10
strings = ["apple", "banana", "orange", "watermelon", "grape"]

for string in strings:
    slot = simple_hash(string, table_size)
    print(f"The hash value for '{string}' is {slot}")

#     The hash value for 'apple' is 0
#        The ASCII values of the characters in 'apple' are: a=97, p=112, p=112, l=108, e=101
#        Summing these ASCII values: 97 + 112 + 112 + 108 + 101 = 530
#        Modulus with table size 10: 530 % 10 = 0

#    The hash value for 'banana' is 9
#        The ASCII values of the characters in 'banana' are: b=98, a=97, n=110, a=97, n=110, a=97
#        Summing these ASCII values: 98 + 97 + 110 + 97 + 110 + 97 = 609
#        Modulus with table size 10: 609 % 10 = 9

#    The hash value for 'orange' is 6
#        The ASCII values of the characters in 'orange' are: o=111, r=114, a=97, n=110, g=103, e=101
#        Summing these ASCII values: 111 + 114 + 97 + 110 + 103 + 101 = 636
#        Modulus with table size 10: 636 % 10 = 6

#    The hash value for 'watermelon' is 6
#        The ASCII values of the characters in 'watermelon' are: w=119, a=97, t=116, e=101, r=114, m=109, e=101, l=108, o=111, n=110
#        Summing these ASCII values: 119 + 97 + 116 + 101 + 114 + 109 + 101 + 108 + 111 + 110 = 1086
#        Modulus with table size 10: 1086 % 10 = 6

#    The hash value for 'grape' is 7
#        The ASCII values of the characters in 'grape' are: g=103, r=114, a=97, p=112, e=101
#        Summing these ASCII values: 103 + 114 + 97 + 112 + 101 = 527
#        Modulus with table size 10: 527 % 10 = 7