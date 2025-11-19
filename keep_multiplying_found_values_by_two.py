"""
LeetCode
2154. Keep Multiplying Found Values by Two
November 2025 Challenge
jramaswami
"""


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums0 = set(nums)
        while original in nums0:
            original *= 2
        return original