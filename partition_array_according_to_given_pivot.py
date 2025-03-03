"""
LeetCode
2161. Partition Array According to Given Pivot
March 2025 Challenge
jramaswami
"""


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        middle = []
        right = []
        for n in nums:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                middle.append(n)
        i = 0
        for n in left:
            nums[i] = n
            i += 1
        for n in middle:
            nums[i] = n
            i += 1
        for n in right:
            nums[i] = n
            i += 1
        return nums
