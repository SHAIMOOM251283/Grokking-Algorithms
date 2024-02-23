from collections import deque

def bfs_shortest_path(graph, start, goal):
    # Check if start and goal nodes are in the graph
    if start not in graph or goal not in graph:
        return None

    # Queue for BFS
    queue = deque()
    queue.append((start, [start]))  # (node, path)
    
    # Visited nodes
    visited = set()

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        # Check if we've reached the goal
        if node == goal:
            return path

        # Enqueue neighboring nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    # If goal is not reachable from start
    return None

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
goal_node = 'F'

shortest_path = bfs_shortest_path(graph, start_node, goal_node)
if shortest_path:
    print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(shortest_path)}")
else:
    print(f"No path found from {start_node} to {goal_node}")
