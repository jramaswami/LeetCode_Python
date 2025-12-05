"""
LeetCode
3432. Count Partitions with Even Sum Difference
December 2025 Challenge
jramaswami
"""


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        soln = left = 0
        for n in nums[:-1]:
            left += n
            right = total - left
            if (left - right) % 2 == 0:
                soln += 1
        return soln