import heapq

def dijkstra(graph, start):
    # Step 1: Initialize the costs and the paths
    costs = {node: float('inf') for node in graph}
    costs[start] = 0
    path = {}

    # Step 2: Create a priority queue to track the nodes with their respective costs
    priority_queue = [(0, start)]  # (cost, node)
    
    while priority_queue:
        # Step 1: Find the cheapest node
        current_cost, current_node = heapq.heappop(priority_queue)
        
        # Step 3: Check whether there’s a cheaper path to the neighbors of this node
        for neighbor, weight in graph[current_node].items():
            new_cost = current_cost + weight
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                path[neighbor] = current_node
                heapq.heappush(priority_queue, (new_cost, neighbor))
    
    # Step 4: Calculate the final path
    final_path = []
    node = max(costs, key=costs.get)  # Find the node with the maximum cost
    while node:
        final_path.append(node)
        node = path.get(node)
    final_path.reverse()
    
    return final_path, costs

# Example graph
graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'C': 5, 'D': 2, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'C': 5, 'D': 1}
}

start_node = 'A'
final_path, costs = dijkstra(graph, start_node)
print("Final Path:", final_path)
print("Costs:", costs)
