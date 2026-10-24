''' write a program to Construct a Graph class with kruskal_mst() -> List[Edge] and prim_mst() -> List[Edge]
methods that process edge-weighted graph structures and return the MST edge set.'''


# Program 6: Kruskal's and Prim's MST

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    # Add edge to graph
    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    # Kruskal's Algorithm
    def kruskal_mst(self):
        parent = list(range(self.vertices))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                parent[root_y] = root_x
                return True

            return False

        mst = []

        # Sort edges by weight
        edges = sorted(self.edges, key=lambda edge: edge[2])

        for u, v, weight in edges:
            if union(u, v):
                mst.append((u, v, weight))

        return mst

    # Prim's Algorithm
    def prim_mst(self):
        visited = [False] * self.vertices
        mst = []

        visited[0] = True

        while len(mst) < self.vertices - 1:
            minimum = float('inf')
            selected_edge = None

            for u, v, weight in self.edges:

                if visited[u] and not visited[v]:
                    if weight < minimum:
                        minimum = weight
                        selected_edge = (u, v, weight)

                elif visited[v] and not visited[u]:
                    if weight < minimum:
                        minimum = weight
                        selected_edge = (v, u, weight)

            if selected_edge is None:
                break

            u, v, weight = selected_edge

            mst.append((u, v, weight))
            visited[v] = True

        return mst


# Main Program
g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

# Kruskal's MST
print("Kruskal's MST:")

kruskal_result = g.kruskal_mst()

total = 0

for u, v, weight in kruskal_result:
    print(u, "-", v, ":", weight)
    total += weight

print("Total Cost:", total)


# Prim's MST
print("\nPrim's MST:")

prim_result = g.prim_mst()

total = 0

for u, v, weight in prim_result:
    print(u, "-", v, ":", weight)
    total += weight

print("Total Cost:", total)
