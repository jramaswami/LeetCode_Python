"""
LeetCode :: June 2021 Challenge :: Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
jramaswami
"""


from typing import *


MOD = pow(10, 9) + 7


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts0 = [0] + sorted(horizontalCuts) + [h]
        verticalCuts0 = [0] + sorted(verticalCuts) + [w]
        maxDh = max(b - a for a, b in zip(horizontalCuts0, horizontalCuts0[1:]))
        maxDw = max(b - a for a, b in zip(verticalCuts0, verticalCuts0[1:]))
        return (maxDh * maxDw) % MOD


def test_1():
    h = 5
    w = 4
    horizontalCuts = [1,2,4]
    verticalCuts = [1,3]
    assert Solution().maxArea(h, w, horizontalCuts, verticalCuts) == 4


def test_2():
    h = 5
    w = 4
    horizontalCuts = [3,1]
    verticalCuts = [1]
    assert Solution().maxArea(h, w, horizontalCuts, verticalCuts) == 6


def test_3():
    h = 5
    w = 4
    horizontalCuts = [3]
    verticalCuts = [3]
    assert Solution().maxArea(h, w, horizontalCuts, verticalCuts) == 9
