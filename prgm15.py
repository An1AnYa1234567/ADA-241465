''' Write a program to build a GraphBacktracker class featuring graph_coloring(m: int) -> List[int] and
hamiltonian_cycle() -> List[int] methods returning vertex-color mappings and valid path cycles.'''

from typing import List
class GraphBacktracker:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
    # Check whether a color can be assigned
    def is_safe_color(self, vertex, color, colors):
        for i in range(self.n):
            if self.graph[vertex][i] == 1 and colors[i] == color:
                return False
        return True
    # Graph Coloring
    def graph_coloring(self, m: int) -> List[int]:
        colors = [0] * self.n

        def backtrack(vertex):
            if vertex == self.n:
                return True

            for color in range(1, m + 1):
                if self.is_safe_color(vertex, color, colors):
                    colors[vertex] = color

                    if backtrack(vertex + 1):
                        return True

                    colors[vertex] = 0

            return False

        if backtrack(0):
            return colors

        return []
    # Check whether a vertex can be added to the cycle
    def is_safe_cycle(self, vertex, path, position):
        if self.graph[path[position - 1]][vertex] == 0:
            return False

        if vertex in path:
            return False

        return True
    # Hamiltonian Cycle
    def hamiltonian_cycle(self) -> List[int]:
        if self.n == 0:
            return []

        path = [0] * (self.n + 1)
        path[0] = 0

        def backtrack(position):
            if position == self.n:
                if self.graph[path[position - 1]][path[0]] == 1:
                    path[position] = path[0]
                    return True
                return False

            for vertex in range(1, self.n):
                if self.is_safe_cycle(vertex, path, position):
                    path[position] = vertex

                    if backtrack(position + 1):
                        return True

                    path[position] = -1

            return False

        if backtrack(1):
            return path

        return []
# Main Program
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]
g = GraphBacktracker(graph)
# Graph Coloring
m = 3
coloring = g.graph_coloring(m)
print("Graph Coloring:", coloring)
# Hamiltonian Cycle
cycle = g.hamiltonian_cycle()
if cycle:
    print("Hamiltonian Cycle:", cycle)
else:
    print("No Hamiltonian Cycle exists")
