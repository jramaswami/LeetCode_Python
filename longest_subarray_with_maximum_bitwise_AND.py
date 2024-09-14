"""
LeetCode
2419. Longest Subarray With Maximum Bitwise AND
September 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        window = collections.deque()
        deficient_count = 0
        soln = 0
        for n in nums:
            if n < max_val:
                window.clear()
            else:
                window.append(n)
            soln = max(soln, len(window))
        return soln
