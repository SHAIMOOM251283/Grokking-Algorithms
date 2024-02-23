class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.child_pointers = []


class BTree:
    def __init__(self, degree):
        self.root = BTreeNode(True)
        self.degree = degree

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.degree) - 1:
            new_root = BTreeNode(False)
            new_root.child_pointers.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.child_pointers[i].keys) == (2 * self.degree) - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.child_pointers[i], key)

    def split_child(self, parent, i):
        degree = self.degree
        child = parent.child_pointers[i]
        new_child = BTreeNode(child.leaf)
        parent.child_pointers.insert(i + 1, new_child)
        parent.keys.insert(i, child.keys[degree - 1])
        new_child.keys = child.keys[degree:(2 * degree) - 1]
        child.keys = child.keys[0:degree - 1]
        if not child.leaf:
            new_child.child_pointers = child.child_pointers[degree:2 * degree]
            child.child_pointers = child.child_pointers[0:degree - 1]

    def print_tree(self, node, level=0):
        if node:
            print("Level", level, ":", ",".join(str(key) for key in node.keys))
            if not node.leaf:
                for i in range(len(node.child_pointers)):
                    self.print_tree(node.child_pointers[i], level + 1)

# Example usage
if __name__ == "__main__":
    b_tree = BTree(degree=3)
    keys = [10, 20, 5, 6, 12, 30, 7, 17]
    for key in keys:
        b_tree.insert(key)
    print("B-tree:")
    b_tree.print_tree(b_tree.root)

# The left child node contains keys smaller than the root node key (10),
# while the right child node contains keys greater than the root node key.
