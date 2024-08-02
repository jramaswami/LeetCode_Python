"""
LeetCode
2134. Minimum Swaps to Group All 1's Together II
August 2024 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        nums0 = nums + nums
        window = collections.deque()
        curr_ones = 0
        soln = pow(10, 10)
        for n in nums0:
            window.append(n)
            curr_ones += n
            while len(window) > ones:
                curr_ones -= window.popleft()
            if len(window) == ones:
                soln = min(soln, ones - curr_ones)
        return soln