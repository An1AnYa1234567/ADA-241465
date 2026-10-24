''' Write a program to create a TSPSolver class with solve_tsp(dist_matrix: List[List[int]]) -> int taking an
adjacency matrix and returning the minimum tour cost.'''

# Travelling Salesman Problem (TSP)
def tsp_solver(graph):
    n = len(graph)
    INF = float('inf')

    # dp[mask][city] stores minimum cost
    dp = [[INF] * n for _ in range(1 << n)]

    # Start from city 0
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):

            if dp[mask][u] == INF:
                continue

            for v in range(n):

                # Visit an unvisited city
                if not (mask & (1 << v)):
                    new_mask = mask | (1 << v)

                    dp[new_mask][v] = min(
                        dp[new_mask][v],
                        dp[mask][u] + graph[u][v]
                    )

    # Return to starting city
    full_mask = (1 << n) - 1

    minimum_cost = min(
        dp[full_mask][city] + graph[city][0]
        for city in range(1, n)
    )

    return minimum_cost
# Main Program
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
result = tsp_solver(graph)
print("Minimum Travelling Cost:", result)
