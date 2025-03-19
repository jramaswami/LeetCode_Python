"""
LeetCode
3191. Minimum Operations to Make Binary Array Elements Equal to One I
March 2025 Challenge
jramaswami
"""


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        soln = 0
        for i, n in enumerate(nums):
            if i + 2 >= len(nums):
                break
            if n == 0:
                soln += 1
                for d in range(3):
                    if nums[i+d] == 0:
                        nums[i+d] = 1
                    else:
                        nums[i+d] = 0
        if all(n == 1 for n in nums):
            return soln
        return -1