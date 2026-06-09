"""
LeetCode
3689. Maximum Total Subarray Value I
June 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        min_x = min(nums)
        max_x = max(nums)
        return k * (max_x - min_x)