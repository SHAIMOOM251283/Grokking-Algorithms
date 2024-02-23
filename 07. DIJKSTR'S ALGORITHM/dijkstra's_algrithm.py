import heapq

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity except start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to keep track of the next node to visit
    pq = [(0, start)]
    
    while pq:
        # Get the current node with the smallest distance from the start node
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if we have already found a shorter path to this node
        if current_distance > distances[current_node]:
            continue
            
        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'C': 1, 'D': 7},
    'C': {'D': 3},
    'D': {'E': 1},
    'E': {}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node + ":")
for node, distance in distances.items():
    print("To node", node + ":", distance)
