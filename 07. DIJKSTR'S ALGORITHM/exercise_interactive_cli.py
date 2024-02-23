import heapq

def dijkstra(graph, start, end):
    # Initialize distances with infinity for all nodes except start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to store nodes to visit
    pq = [(0, start)]  # (distance, node)
    
    # Dictionary to store parent nodes for each node in the shortest path
    parents = {node: None for node in graph}
    
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
                # Update parent for the neighbor
                parents[neighbor] = current_node
    
    # Reconstruct the shortest path
    shortest_path = []
    current = end
    while current is not None:
        shortest_path.append(current)
        current = parents[current]
    shortest_path.reverse()
    
    # Return the shortest distance and the shortest path
    return distances[end], shortest_path

def create_graph():
    graph = {}
    nodes = int(input("Enter the number of nodes: "))
    
    for i in range(nodes):
        node = input(f"Enter name of node {i+1}: ")
        neighbors = {}
        num_neighbors = int(input(f"Enter the number of neighbors for node {node}: "))
        for j in range(num_neighbors):
            neighbor, weight = input(f"Enter neighbor {j+1} and its weight separated by space: ").split()
            neighbors[neighbor] = int(weight)
        graph[node] = neighbors
    
    return graph

def main():
    # Create the graph
    graph = create_graph()
    
    # Get start and end nodes from user
    start = input("Enter start node: ")
    end = input("Enter end node: ")
    
    # Calculate the shortest path from start to end
    shortest_distance, shortest_path = dijkstra(graph, start, end)
    
    # Print the result
    print("Shortest distance from", start, "to", end, ":", shortest_distance)
    print("Shortest path:", shortest_path)

if __name__ == "__main__":
    main()
