'''write a program to Build a ShortestPath class containing dijkstra(src: int) -> List[int] and
bellman_ford(src: int) -> List[int] methods taking a starting node and returning distance
arrays (or error status for negative cycles). '''

# Dijkstra's and Bellman-Ford
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
    # Add edge to graph
    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))
    # Dijkstra's Algorithm
    def dijkstra(self, src):
        dist = [float('inf')] * self.vertices
        visited = [False] * self.vertices

        dist[src] = 0

        for _ in range(self.vertices):

            minimum = float('inf')
            u = -1

            # Find minimum distance vertex
            for i in range(self.vertices):
                if not visited[i] and dist[i] < minimum:
                    minimum = dist[i]
                    u = i

            if u == -1:
                break

            visited[u] = True

            # Update adjacent vertices
            for a, b, weight in self.edges:
                if a == u and not visited[b]:
                    if dist[u] + weight < dist[b]:
                        dist[b] = dist[u] + weight

                elif b == u and not visited[a]:
                    if dist[u] + weight < dist[a]:
                        dist[a] = dist[u] + weight

        return dist
    # Bellman-Ford Algorithm
    def bellman_ford(self, src):
        dist = [float('inf')] * self.vertices
        dist[src] = 0

        # Relax all edges
        for _ in range(self.vertices - 1):

            for u, v, weight in self.edges:

                if dist[u] != float('inf'):
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight

                if dist[v] != float('inf'):
                    if dist[v] + weight < dist[u]:
                        dist[u] = dist[v] + weight

        # Check negative weight cycle
        for u, v, weight in self.edges:

            if dist[u] != float('inf'):
                if dist[u] + weight < dist[v]:
                    return "Negative weight cycle detected"

            if dist[v] != float('inf'):
                if dist[v] + weight < dist[u]:
                    return "Negative weight cycle detected"

        return dist
# Main Program
g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 5)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 1, 3)
g.add_edge(2, 3, 9)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 4)
g.add_edge(4, 3, 6)

source = 0

print("Dijkstra's Algorithm:")
print(g.dijkstra(source))

print("\nBellman-Ford Algorithm:")
print(g.bellman_ford(source))
