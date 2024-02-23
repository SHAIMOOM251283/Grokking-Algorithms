import numpy as np

def nearest_neighbor_tsp(distances):
    n = len(distances)
    unvisited = set(range(n))
    tour = []
    
    # Start at a random city
    current_city = np.random.choice(list(unvisited))
    tour.append(current_city)
    unvisited.remove(current_city)
    
    # Repeat until all cities have been visited
    while unvisited:
        nearest_city = min(unvisited, key=lambda city: distances[current_city][city])
        tour.append(nearest_city)
        unvisited.remove(nearest_city)
        current_city = nearest_city
    
    # Return to the starting city to complete the tour
    tour.append(tour[0])
    
    return tour

# Example distances between cities (replace with actual distances)
distances = np.array([
    [0, 2, 3, 4],
    [2, 0, 6, 7],
    [3, 6, 0, 9],
    [4, 7, 9, 0]
])

# Run nearest neighbor TSP algorithm
tour = nearest_neighbor_tsp(distances)
print("Approximate TSP tour:", tour)
