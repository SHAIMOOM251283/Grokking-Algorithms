import numpy as np

def nearest_neighbor(distances):
    n = len(distances)
    unvisited = set(range(1, n))
    tour = [0]
    current_node = 0
    
    while unvisited:
        nearest_node = min(unvisited, key=lambda x: distances[current_node][x])
        tour.append(nearest_node)
        unvisited.remove(nearest_node)
        current_node = nearest_node
    
    tour.append(0)  # Return to the starting point to complete the tour
    return tour

# Example distances between homes (replace with actual distances)
distances = np.array([
    [0, 2, 3, 4, 5],
    [2, 0, 6, 7, 8],
    [3, 6, 0, 9, 10],
    [4, 7, 9, 0, 11],
    [5, 8, 10, 11, 0]
])

tour = nearest_neighbor(distances)
print("Shortest route:", tour)
