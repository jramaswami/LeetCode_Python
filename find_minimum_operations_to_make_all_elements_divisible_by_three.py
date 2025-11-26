"""
LeetCode
3190. Find Minimum Operations to Make All Elements Divisible by Three
November 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(min(n % 3, 3 - n % 3) for n in nums)