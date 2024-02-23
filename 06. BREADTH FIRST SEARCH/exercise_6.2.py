from collections import deque

# Graph represented as adjacency list
graph = {
    'CAB': ['CAT', 'CAR'],
    'CAT': ['BAT', 'MAT', 'CAR'],
    'CAR': ['CAT', 'BAR'],
    'MAT': ['BAT'],
    'BAR': ['BAT']
}

def bfs_shortest_path(graph, start, end):
    # Queue for BFS
    queue = deque()
    # Path dictionary to store the predecessor of each node
    path_dict = {}
    # Visited set to avoid cycles
    visited = set()

    # Start BFS with the start node
    queue.append(start)
    visited.add(start)

    # Continue BFS until the queue is empty
    while queue:
        current_node = queue.popleft()

        # If we reach the end node, reconstruct and return the shortest path
        if current_node == end:
            shortest_path = []
            while current_node != start:
                shortest_path.append(current_node)
                current_node = path_dict[current_node]
            shortest_path.append(start)
            shortest_path.reverse()
            return shortest_path

        # Explore neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                path_dict[neighbor] = current_node

    # If no path found, return None
    return None

def find_shortest_path_length(graph, start, end):
    shortest_path = bfs_shortest_path(graph, start, end)
    if shortest_path:
        return len(shortest_path) - 1  # Length of path is number of edges, which is nodes - 1
    else:
        return float('inf')  # No path found

# Find shortest path length from CAB to BAT
start_node = 'CAB'
end_node = 'BAT'
shortest_path_length = find_shortest_path_length(graph, start_node, end_node)

# Output all paths and their lengths
print("All paths from {} to {}:".format(start_node, end_node))
for node, neighbors in graph.items():
    for neighbor in neighbors:
        path_length = find_shortest_path_length(graph, node, neighbor)
        print("{} > {} (Length: {})".format(node, neighbor, path_length))

print("\nShortest path from {} to {}: (Length: {})".format(start_node, end_node, shortest_path_length))
shortest_path = bfs_shortest_path(graph, start_node, end_node)
print(" > ".join(shortest_path))
