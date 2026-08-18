'''Program-3 WAP to Implement findKthLargest(nums: List[int], k: int) -> int and 
findMinMax(nums: List[int]) -> Tuple[int, int] functions accepting an unsorted array, 
returning the n-th element and min-max pair. using divide and conquer and analysis in python'''
from typing import List, Tuple
def findKthLargest(nums: List[int], k: int) -> int:
    target = len(nums) - k
    def quick_select(left, right):
        pivot = nums[right]
        p = left
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[right] = nums[right], nums[p]
        if p == target:
            return nums[p]
        elif p < target:
            return quick_select(p + 1, right)
        else:
            return quick_select(left, p - 1)

    return quick_select(0, len(nums) - 1)

def findMinMax(nums: List[int]) -> Tuple[int, int]:

    def divide(left, right):
        if left == right:
            return nums[left], nums[left]

        if right == left + 1:
            return (
                min(nums[left], nums[right]),
                max(nums[left], nums[right])
            )

        mid = (left + right) // 2

        min1, max1 = divide(left, mid)
        min2, max2 = divide(mid + 1, right)

        return min(min1, min2), max(max1, max2)

    return divide(0, len(nums) - 1)
# Main function
nums = [7, 2, 9, 1, 5, 4]
print("Array:", nums)
k = 2
print(k, "th Largest:", findKthLargest(nums.copy(), k))
minimum, maximum = findMinMax(nums)
print("Minimum:", minimum)
print("Maximum:", maximum)