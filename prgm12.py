''' Write a program to implement floyd_warshall(graph: List[List[int]])-> List[List[int]] and
optimal_bst(keys: List[int], freq: List[int]) -> int accepting distance/frequency
matrices and returning shortest path or cost matrices.'''

# Floyd-Warshall and Optimal BST
# Floyd-Warshall Algorithm
def floyd_warshall(graph):
    n = len(graph)
    # Copy graph into distance matrix
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    return dist
# Optimal Binary Search Tree
def optimal_bst(keys, freq):
    n = len(keys)

    if n == 0:
        return 0

    # DP table
    cost = [[0] * n for _ in range(n)]

    # Prefix sums for frequency ranges
    prefix = [0]
    for f in freq:
        prefix.append(prefix[-1] + f)

    # Cost of trees containing one key
    for i in range(n):
        cost[i][i] = freq[i]

    # Consider chains of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total_freq = prefix[j + 1] - prefix[i]
            cost[i][j] = float('inf')

            for r in range(i, j + 1):
                left = cost[i][r - 1] if r > i else 0
                right = cost[r + 1][j] if r < j else 0

                current = left + right + total_freq
                cost[i][j] = min(cost[i][j], current)

    return cost[0][n - 1]
# Main Program
# Example 1: Floyd-Warshall
INF = float('inf')
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
print("Floyd-Warshall Shortest Path Matrix:")
result = floyd_warshall(graph)

for row in result:
    print([x if x != INF else "INF" for x in row])
# Example 2: Optimal BST
keys = [10, 20, 30]
freq = [34, 8, 50]

print("\nOptimal BST Minimum Search Cost:",
      optimal_bst(keys, freq))
