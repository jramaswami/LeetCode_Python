"""
LeetCode
2110. Number of Smooth Descent Periods of a Stock
December 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        window = collections.deque()
        soln = 0

        def S(x):
            return (x * (x + 1)) // 2

        for n in prices:
            if window and n != window[-1] - 1:
                soln += S(len(window))
                window.clear()
            window.append(n)
        soln += S(len(window))
        return soln