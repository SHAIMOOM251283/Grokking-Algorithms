# Define a function to calculate the length of the shortest path
def shortest_path_length(path):
    # Initialize the total length
    total_length = 0
    
    # Loop through each node in the path
    for i in range(len(path) - 1):
        # Increment the total length by the length of the edge from the current node to the next node
        if path[i] == 'Start' and path[i+1] == 'B':
            total_length += 1
        elif path[i] == 'B' and path[i+1] == 'Finish':
            total_length += 1
        elif path[i] == 'Start' and path[i+1] == 'C':
            total_length += 1
        elif path[i] == 'C' and path[i+1] == 'D':
            total_length += 1
        elif path[i] == 'D' and path[i+1] == 'Finish':
            total_length += 1
        elif path[i] == 'C' and path[i+1] == 'A':
            total_length += 1
        elif path[i] == 'A' and path[i+1] == 'B':
            total_length += 1
    
    return total_length

# Paths to be evaluated
paths = [
    ['Start', 'B', 'Finish'],
    ['Start', 'B', 'A', 'C', 'D', 'Finish'],
    ['Start', 'C', 'D', 'Finish'],
    ['Start', 'C', 'A', 'B', 'Finish']
]

# Initialize variables to store the shortest path and its length
shortest_path = None
shortest_length = float('inf')

# Calculate the length of each path and find the shortest one
for path in paths:
    length = shortest_path_length(path)
    if length < shortest_length:
        shortest_path = path
        shortest_length = length

    # Output the current path
    print(f"Path: {path}, Length: {length}")

# Output the shortest path
print(f"\nThe shortest path is {shortest_path} with a length of {shortest_length}.")
