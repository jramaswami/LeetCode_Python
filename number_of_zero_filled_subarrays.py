"""
LeetCode
2348. Number of Zero-Filled Subarrays
August 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        soln = 0
        curr_sum = 0
        window = collections.deque()
        for n in nums:
            curr_sum += n
            window.append(n)
            while curr_sum:
                curr_sum -= window[0]
                window.popleft()
            soln += len(window)
        return soln