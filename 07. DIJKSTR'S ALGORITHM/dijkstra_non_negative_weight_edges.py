import heapq

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    # Distance from the start node to itself is 0
    distances[start] = 0
    # Priority queue to keep track of nodes to visit
    pq = [(0, start)]

    while pq:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)

        # Check all neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If the new distance is smaller than the current known distance to the neighbor
            if distance < distances[neighbor]:
                # Update the distance
                distances[neighbor] = distance
                # Add the neighbor to the priority queue
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 9},
    'C': {'D': 2},
    'D': {}
}

start_node = 'A'
print("Shortest distances from node", start_node, ":", dijkstra(graph, start_node))
