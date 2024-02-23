import heapq

def dijkstra(graph, start):
    # Step 1: Initialize distances to infinity for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Step 2: Priority queue to store nodes with their current distance from the start node
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Step 1: Find the node with the shortest distance from the start node
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip if current distance is greater than already known distance
        if current_distance > distances[current_node]:
            continue
        
        # Step 3: Explore neighbors of current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If a shorter path is found to the neighbor, update the distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Add the neighbor to the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Step 4: Final distances calculated
    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 3, 'C': 4},
    'B': {'C': 1, 'D': 6},
    'C': {'D': 2},
    'D': {'B': 1}
}

# Starting node
start_node = 'A'

# Run Dijkstra's algorithm
shortest_distances = dijkstra(graph, start_node)

# Print the shortest distances
print("Shortest distances from node", start_node + ":")
for node, distance in shortest_distances.items():
    print("To node", node + ":", distance)
