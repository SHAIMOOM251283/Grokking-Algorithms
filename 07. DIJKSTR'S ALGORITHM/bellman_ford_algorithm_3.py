def bellman_ford(graph, source):
    """
    Implements the Bellman-Ford algorithm to find the shortest paths from a source node to all other nodes in a graph.

    Args:
      graph: A dictionary representing the graph, where keys are nodes and values are dictionaries mapping neighbors to edge weights.
      source: The source node.

    Returns:
      A dictionary mapping nodes to their distances from the source node, or None if a negative cycle is detected.
    """
    n = len(graph)
    distance = {node: float('inf') for node in graph}
    distance[source] = 0

    for _ in range(n - 1):
        for node, neighbors in graph.items():
            for neighbor, weight in neighbors.items():
                distance[neighbor] = min(distance[neighbor], distance[node] + weight)

    # Check for negative cycles
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            if distance[neighbor] > distance[node] + weight:
                return None

    return distance


def main():
    graph = {
        'A': {'B': -1, 'C': 4},
        'B': {'D': 2, 'E': 3},
        'C': {'D': -2},
        'D': {'E': 1},
        'E': {}
    }

    source = input("Enter the source node: ")

    shortest_paths = bellman_ford(graph, source)

    if shortest_paths is None:
        print("Negative cycle detected!")
    else:
        for node, distance in shortest_paths.items():
            print(f"Shortest path from {source} to {node}: {distance}")


if __name__ == "__main__":
    main()

# inf: stands for infinity, not an infinite loop. 
# It indicates that there is no path from the source node to the destination node within the given graph.