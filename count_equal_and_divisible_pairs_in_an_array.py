"""
LeetCode
2176. Count Equal and Divisible Pairs in an Array
April 2025 Challenge
jramaswami
"""


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        soln = 0
        for i, _ in enumerate(nums):
            for j, _ in enumerate(nums):
                if i < j and nums[i] == nums[j] and (i * j) % k == 0:
                    soln += 1
        return soln