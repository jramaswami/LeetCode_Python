"""
LeetCode
1493. Longest Subarray of 1's After Deleting One Element
July 2023 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window = collections.deque()
        zeroes = 0
        soln = 0
        for n in nums:
            window.append(n)
            if n == 0:
                zeroes += 1
            while zeroes > 1:
                if window[0] == 0:
                    zeroes -= 1
                window.popleft()
            soln = max(soln, len(window) - 1)
        return soln