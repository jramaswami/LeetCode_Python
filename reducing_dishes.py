"""
LeetCode
1402. Reducing Dishes
March 2023 Challenge
jramaswami
"""


import itertools
from typing import *


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        prefix_sum = list(itertools.accumulate(satisfaction))
        N = len(satisfaction)
        curr = sum((N-i)*x for i, x in enumerate(satisfaction))
        while prefix_sum and curr - prefix_sum[-1] > curr:
            curr -= prefix_sum[-1]
            prefix_sum.pop()
        return curr


def test_1():
    satisfaction = [-1,-8,0,5,-9]
    expected = 14
    assert Solution().maxSatisfaction(satisfaction) == expected


def test_2():
    satisfaction = [4,3,2]
    expected = 20
    assert Solution().maxSatisfaction(satisfaction) == expected


def test_3():
    satisfaction = [-1, -4, -5]
    expected = 0
    assert Solution().maxSatisfaction(satisfaction) == expected