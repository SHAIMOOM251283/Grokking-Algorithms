import heapq

def dijkstra(graph, start, end):
    # Initialize distances with infinity for all nodes except start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to store nodes to visit
    pq = [(0, start)]  # (distance, node)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Check if the current node's distance is already smaller than calculated
        if current_distance > distances[current_node]:
            continue
        
        # Iterate through neighbors of current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If the new distance is smaller, update distance and push into priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    # Return the shortest distance to the end node
    return distances[end]

# Define the graph
graph = {
    'Start': {'A': 2, 'B': 2},
    'A': {'C': 2, 'Finish': 2},
    'B': {'A': 2},
    'C': {'B': -1, 'Finish': 2},
    'Finish': {}
}

# Calculate the shortest path from 'Start' to 'Finish'
shortest_distance = dijkstra(graph, 'Start', 'Finish')
print("Shortest distance from Start to Finish:", shortest_distance)
