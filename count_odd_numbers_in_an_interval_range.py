"""
LeetCode
1523. Count Odd Numbers in an Interval Range
February 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 == 1:
            high += 1
        return (high // 2) - (low // 2)


def test_1():
    low = 3
    high = 7
    expected = 3
    assert Solution().countOdds(low, high)


def test_2():
    low = 8
    high = 10
    expected = 1
    assert Solution().countOdds(low, high)