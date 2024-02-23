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

def parse_graph_input():
    graph = {}
    while True:
        line = input("Enter node and its neighbors (node: neighbor1 neighbor2 ...), or type 'done' to finish: ")
        if line.lower() == 'done':
            break
        parts = line.split(':')
        node = parts[0].strip()
        neighbors = [n.strip() for n in parts[1].split()]
        graph[node] = neighbors
    return graph

def main():
    print("Enter the graph:")
    graph = parse_graph_input()

    start_node = input("Enter the start node: ").strip()
    goal_node = input("Enter the goal node: ").strip()

    shortest_path = bfs_shortest_path(graph, start_node, goal_node)
    if shortest_path:
        print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(shortest_path)}")
    else:
        print(f"No path found from {start_node} to {goal_node}")

if __name__ == "__main__":
    main()



#Enter node and its neighbors (node: neighbor1 neighbor2 ...), or type 'done' to finish: A: B C
#Enter node and its neighbors (node: neighbor1 neighbor2 ...), or type 'done' to finish: B: A D E
#Enter node and its neighbors (node: neighbor1 neighbor2 ...), or type 'done' to finish: C: A F
#Enter node and its neighbors (node: neighbor1 neighbor2 ...), or type 'done' to finish: D: B
#Enter node and its neighbors (node: neighbor1 neighbor2 ...), or type 'done' to finish: E: B F
#Enter node and its neighbors (node: neighbor1 neighbor2 ...), or type 'done' to finish: F: C E
#Enter node and its neighbors (node: neighbor1 neighbor2 ...), or type 'done' to finish: done
#Enter the start node: A
#Enter the goal node: F
#Shortest path from A to F: A -> C -> F
