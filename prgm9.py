''' write a program to implement knapsack_01(weights: List[int], values: List[int], capacity: int) -> int
utilizing 2D/1D DP methods that accept item properties and return maximum value.'''

# 0/1 Knapsack using Dynamic Programming
def knapsack_01(weights, values, capacity):
    n = len(weights)
    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
# Main Program
weights = [10, 20, 30, 5]
values = [60, 100, 120, 50]
capacity = 15
result = knapsack_01(weights, values, capacity)
print("Weights:", weights)
print("Values:", values)
print("Capacity:", capacity)
print("Maximum Profit:", result)
