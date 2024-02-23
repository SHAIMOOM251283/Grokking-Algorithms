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

# Accessing and modifying elements using a loop
while True:
    my_linked_list.display()

    # Taking user choice
    choice = input("Do you want to access or modify elements? (Type 'access', 'modify', or 'exit'): ").lower()

    if choice == 'access':
        # Accessing elements
        index = int(input("Enter the index to access: "))
        current = my_linked_list.head
        for _ in range(index):
            if current is not None:
                current = current.next_node

        if current is not None:
            print(f"Element at index {index} is: {current.data}")
        else:
            print("Invalid index. Please enter a valid index.")

    elif choice == 'modify':
        # Modifying elements
        index = int(input("Enter the index to modify: "))
        current = my_linked_list.head
        for _ in range(index):
            if current is not None:
                current = current.next_node

        if current is not None:
            new_value = int(input("Enter the new value: "))
            current.data = new_value
            print("Linked List after modifying the element at index", index, ":")
            my_linked_list.display()
        else:
            print("Invalid index. Please enter a valid index.")

    elif choice == 'exit':
        break

    else:
        print("Invalid choice. Please enter 'access', 'modify', or 'exit'.")

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
