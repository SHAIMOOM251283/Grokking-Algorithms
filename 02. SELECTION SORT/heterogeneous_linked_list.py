class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

# Linked List with Different Data Types
size = int(input("Enter the size of the linked list: "))
head_node = None

for i in range(size):
    user_input = input(f"Enter data for node {i + 1}: ")
    new_node = Node(user_input)
    
    # Linking Nodes
    new_node.next_node = head_node
    head_node = new_node

# Accessing and Printing Linked List Elements
current_node = head_node
while current_node is not None:
    print("Node data:", current_node.data)
    current_node = current_node.next_node
