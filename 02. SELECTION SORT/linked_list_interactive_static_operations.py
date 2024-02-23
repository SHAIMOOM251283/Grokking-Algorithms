class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next_node
        print("None")

# Creating a linked list and inserting elements
my_linked_list = LinkedList()
user_input = list(map(int, input("Enter the elements separated by space: ").split()))

for element in user_input:
    my_linked_list.insert(element)

# Accessing elements from the linked list
first_element = my_linked_list.head.data
second_element = my_linked_list.head.next_node.data
print("First Element:", first_element)
print("Second Element:", second_element)

# Modifying elements (assuming we want to modify the third element)
if my_linked_list.head.next_node and my_linked_list.head.next_node.next_node:
    my_linked_list.head.next_node.next_node.data = 10
    print("Linked List after modifying the third element:")
    my_linked_list.display()
else:
    print("Linked List doesn't have enough elements to modify the third element.")

# Length of the linked list
def get_linked_list_length(linked_list):
    current = linked_list.head
    length = 0
    while current:
        length += 1
        current = current.next_node
    return length

linked_list_length = get_linked_list_length(my_linked_list)
print("Length of the Linked List:", linked_list_length)
