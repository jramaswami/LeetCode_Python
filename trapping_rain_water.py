"""
LeetCode :: September 2022 Challenge :: Trapping Rain Water
jramaswami
"""


import itertools


class Solution:
    def trap(self, heights):

        prefix = list(itertools.accumulate(heights, max))
        suffix = list(itertools.accumulate(reversed(heights), max))[::-1]

        soln = 0
        for h, left, right in zip(heights, prefix, suffix):
            delta = max(0, min(left, right) - h)
            soln += delta
        return soln



def test_1():
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    expected = 6
    assert Solution().trap(heights) == expected


def test_2():
    heights = [4,2,0,3,2,5]
    expected = 9
    assert Solution().trap(heights) == expected