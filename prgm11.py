''' Write a program to implement lengthOfLIS(nums: List[int]) -> int function accepting an integer array and
returning the length of the longest strictly increasing subsequence.'''

# Longest Increasing Subsequence
def lengthOfLIS(nums):
    n = len(nums)
    if n == 0:
        return 0
    # Initialize DP array
    dp = [1] * n
    # Calculate LIS length
    for i in range(1, n):
        for j in range(i):

            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
# Main Program
nums = [10, 9, 2, 5, 3, 7, 101, 18]

print("Input Array:", nums)
print("Length of LIS:", lengthOfLIS(nums))
