''' Program 2- WAP to  Design a Sort class containing merge_sort(arr: List[int]) -> List[int] and quick_sort(arr: List[int]) -> List[int]
 methods that accept an unsorted integer array and return the sorted array.'''
class Sort:
# Merge Sort
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result
     # Quick Sort
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[0]

        left = []
        right = []

        for i in arr[1:]:
            if i <= pivot:
                left.append(i)
            else:
                right.append(i)

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)
# Create object
s = Sort()
arr = [5, 2, 8, 1, 3]
print("Original array:", arr)
print("Merge Sort:", s.merge_sort(arr))
print("Quick Sort:", s.quick_sort(arr))