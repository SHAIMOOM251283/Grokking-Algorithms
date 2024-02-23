from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight=None):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Assuming undirected graph

    def bfs_shortest_path(self, start, end):
        visited = set()
        queue = [[start]]
        if start == end:
            return [start]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                neighbours = self.graph[node]
                for neighbour, _ in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == end:
                        return new_path
                visited.add(node)
        return None  # No path found

    def dijkstra_shortest_path(self, start, end):
        min_heap = [(0, start, [])]
        visited = set()
        while min_heap:
            (cost, node, path) = heapq.heappop(min_heap)
            if node not in visited:
                path = path + [node]
                if node == end:
                    return path
                visited.add(node)
                for neighbour, weight in self.graph[node]:
                    if neighbour not in visited:
                        heapq.heappush(min_heap, (cost + weight, neighbour, path))
        return None  # No path found

# Example usage
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 5)
g.add_edge('B', 'D', 10)
g.add_edge('C', 'D', 3)

print("Shortest path using BFS:", g.bfs_shortest_path('A', 'D'))
print("Shortest path using Dijkstra's algorithm:", g.dijkstra_shortest_path('A', 'D'))


# For example, in the line g.add_edge('A', 'B', 4), the edge connecting vertices 'A' and 'B' has a weight of 4. 
# This means that it would typically cost or take 4 units to travel from vertex 'A' to vertex 'B' in the graph.