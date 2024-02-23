class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Creating a linked list with elements 1, 2, 3, 4, 5
my_linked_list = LinkedList()
my_linked_list.head = Node(1)
second_node = Node(2)
third_node = Node(3)
fourth_node = Node(4)
fifth_node = Node(5)

my_linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fifth_node

# Printing the linked list
my_linked_list.print_list()
