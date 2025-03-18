"""
LeetCode
2401. Longest Nice Subarray
March 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        window = collections.deque()
        bits_used = 0
        soln = 0
        for n in nums:
            # Remove elements from the left until there are
            # no overlapping bits with n.  For all bits in
            # bits_used only one element can contribute bits.
            while bits_used & n != 0:
                x = window.popleft()
                bits_used = bits_used & (~x)
            assert bits_used & n == 0
            bits_used = bits_used | n
            window.append(n)
            soln = max(soln, len(window))
        return soln