import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes (people)
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
G.add_nodes_from(people)

# Add edges (connections between people)
edges = [('Alice', 'Bob'), ('Alice', 'Charlie'), ('Bob', 'Charlie'), ('Charlie', 'David'), ('Charlie', 'Eve')]
G.add_edges_from(edges)

# Find the largest clique
largest_clique = max(nx.find_cliques(G), key=len)

print("Largest clique:", largest_clique)
