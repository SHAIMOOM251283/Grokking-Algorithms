class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def splay(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            if root.left is None:
                return root
            if key < root.left.key:
                root.left.left = self.splay(root.left.left, key)
                root = self.rotate_right(root)
            elif key > root.left.key:
                root.left.right = self.splay(root.left.right, key)
                if root.left.right is not None:
                    root.left = self.rotate_left(root.left)
            return root if root.left is None else self.rotate_right(root)
        else:
            if root.right is None:
                return root
            if key < root.right.key:
                root.right.left = self.splay(root.right.left, key)
                if root.right.left is not None:
                    root.right = self.rotate_right(root.right)
            elif key > root.right.key:
                root.right.right = self.splay(root.right.right, key)
                root = self.rotate_left(root)
            return root if root.right is None else self.rotate_left(root)

    def search(self, key):
        self.root = self.splay(self.root, key)
        return self.root.key == key

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        self.root = self.splay(self.root, key)

        if key == self.root.key:
            return

        new_node = Node(key)

        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None

        self.root = new_node

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)


def print_menu():
    print("1. Insert")
    print("2. Search")
    print("3. Inorder Traversal")
    print("4. Exit")


# Example usage
if __name__ == "__main__":
    tree = SplayTree()
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            key = int(input("Enter key to insert: "))
            tree.insert(key)
        elif choice == '2':
            key = int(input("Enter key to search: "))
            if tree.search(key):
                print("Key", key, "found in the tree.")
            else:
                print("Key", key, "not found in the tree.")
        elif choice == '3':
            print("Inorder Traversal of the Splay Tree:")
            tree.inorder_traversal(tree.root)
            print()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
