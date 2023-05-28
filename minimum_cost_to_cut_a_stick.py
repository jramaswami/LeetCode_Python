"""
LeetCode
1547. Minimum Cost to Cut a Stick
May 2023 Challenge
jramaswami
"""


import functools
import math
from typing import *


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        boundaries = [0] + sorted(cuts) + [n]
        @functools.cache
        def rec(left, right):
            # No cuts left to make
            if left + 1 == right:
                return 0

            # What is the length of the current stick?
            stick_length = boundaries[right] - boundaries[left]

            # You can make any of the cuts between the two boundaries.
            # What is the optimal cut to make?
            min_cost = math.inf
            for cut_index in range(left+1, right):
                min_cost = min(
                    min_cost,
                    # The cost of this cut + the best of the left and the best of the right.
                    stick_length + rec(left, cut_index) + rec(cut_index, right)
                )
            return min_cost

        return rec(0, len(boundaries)-1)


def test_1():
    n = 7
    cuts = [1,3,4,5]
    expected = 16
    assert Solution().minCost(n, cuts) == expected


def test_2():
    n = 9
    cuts = [5,6,1,4,2]
    expected = 22
    assert Solution().minCost(n, cuts) == expected