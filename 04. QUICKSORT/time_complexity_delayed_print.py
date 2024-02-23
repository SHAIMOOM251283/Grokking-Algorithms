from time import sleep
def print_items2(list):
    for item in list:
        sleep(1)
        print(item)
# Example usage:
my_list = [1, 2, 3, 4, 5]
print_items2(my_list)
