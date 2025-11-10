"""
LeetCode
3542. Minimum Operations to Convert All Elements to Zero
November 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        def rec(left, right):
            if left >= right:
                return 0

            result = 0
            min_val = min(nums[left:right])
            if min_val != 0:
                result = 1
            i = left
            while i < right:
                while i < right and nums[i] == min_val:
                    i += 1
                j = i
                while j < right and nums[j] != min_val:
                    j += 1
                i = j
            return result

        return rec(0, len(nums))