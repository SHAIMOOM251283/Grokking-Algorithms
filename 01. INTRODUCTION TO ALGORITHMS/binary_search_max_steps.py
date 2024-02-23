import math

def calculate_maximum_steps(list_size):
    max_steps = math.ceil(math.log2(list_size))
    return max_steps

# Example with a list size of 128
list_size = int(input("Enter the size of the sorted list: "))
#list_size = 128
#list_size = 256 
max_steps = calculate_maximum_steps(list_size)

print(f"In a sorted list of {list_size} names, the maximum number of steps for binary search is {max_steps} steps.")


# Maximum steps=⌈log2​(list size)⌉
# In this case, the list size is 128. Therefore:
# Maximum steps=⌈log⁡2(128)
# Let's calculate this:
# Maximum steps=⌈7⌉=7Maximum steps=⌈7⌉=7

# log2​(128)
# 128÷2=64
# 64÷2=32
# 32÷2=16
# 16÷2=8
# 8÷2=4
# 4÷2=2
# 2÷2=1

# 2x = 128

# x = 128/2 = 64
# x = 64/2 = 32
# x = 32/2 = 16
# x = 16/2 = 8
# x = 8/2 = 4
# x = 4/2 = 2
# x = 2/2 = 1

# Repeatedly divided 128 by 2 until result is 1, finding that 2^7=128, which implies log⁡2(128)=7.