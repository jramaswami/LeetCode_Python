"""
LeetCode :: March Challenge 2021 :: Distribute Candies
jramaswami
"""
from typing import *
from collections import Counter


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_ctr = Counter(candyType)
        return min(len(candyType) // 2, len(candy_ctr))


def test_1():
    assert Solution().distributeCandies([1,1,2,2,3,3]) == 3

def test_2():
    assert Solution().distributeCandies([1,1,2,3]) == 2

def test_3():
    assert Solution().distributeCandies([6,6,6,6]) == 1
