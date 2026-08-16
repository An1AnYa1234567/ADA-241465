'''Program 1-Implement search(nums: List[int], target: int) -> int and myPow(x: float, n: int) -> float functions 
 taking an integer array/target and base/exponent pairs, returning index and computed value respectively'''

def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1
# Power function
def myPow(x, n):
    result = 1

    if n < 0:
        x = 1 / x
        n = -n

    for i in range(n):
        result = result * x

    return result
# Examples
print(search([2, 7, 11, 4], 11))
print(myPow(2, 5))