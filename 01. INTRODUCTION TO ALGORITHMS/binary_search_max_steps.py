import math

class MaximumSteps:

    def __init__(self):
        self.list_size = int(input("Enter the size of the sorted list: "))

    def calculate_maximum_steps(self):
        max_steps = math.ceil(math.log2(self.list_size))
        return max_steps

    def output(self):
        result = self.calculate_maximum_steps()
        print(f"In a sorted list of {self.list_size} names, the maximum number of steps for binary search is {result} steps.")
        
if __name__ == '__main__':
    steps = MaximumSteps()
    steps.output()


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