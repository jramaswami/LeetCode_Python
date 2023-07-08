"""
LeetCode
2551. Put Marbles in Bags
July 2023 Challenge
jramaswami

With a little help from Larry!
"""


import heapq
from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # Observation: for a given dividing line, the value on either side
        #              is added to the score.
        dividers = [a + b for a, b in zip(weights[:-1], weights[1:])]
        # We need k - 1 dividers
        maxval = sum(heapq.nlargest(k-1, dividers))
        minval = sum(heapq.nsmallest(k-1, dividers))
        return maxval - minval


def test_1():
    weights = [1,3,5,1]
    k = 2
    expected = 4
    assert Solution().putMarbles(weights, k) == expected


def test_2():
    weights = [1, 3]
    k = 2
    expected = 0
    assert Solution().putMarbles(weights, k) == expected
