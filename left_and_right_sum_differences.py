"""
LeetCode
2574. Left and Right Sum Differences
June 2026 Challenge
jramaswami
"""

from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = []
        curr = 0
        for x in nums:
            left_sum.append(curr)
            curr += x
        right_sum = []
        curr = 0
        for x in reversed(nums):
            right_sum.append(curr)
            curr += x
        right_sum = right_sum[::-1]
        return [abs(left - right) for left, right in zip(left_sum, right_sum)]