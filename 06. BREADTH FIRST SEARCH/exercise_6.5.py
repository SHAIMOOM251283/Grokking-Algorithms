import networkx as nx

# Create a tree
tree = nx.Graph()
tree.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5)])

# Create a graph that is not a tree
graph = nx.Graph()
graph.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Function to check if a graph is a tree
def is_tree(graph):
    return nx.is_tree(graph)

# Function to perform breadth-first search
def bfs(graph, start_node):
    visited = set()
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph.neighbors(node))

    print()

print("Tree:")
print("Is tree:", is_tree(tree))
print("BFS traversal from node 1:")
bfs(tree, 1)

print("\nGraph:")
print("Is tree:", is_tree(graph))
print("BFS traversal from node 1:")
bfs(graph, 1)
