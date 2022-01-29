"""
LeetCode :: January 2022 Challenge :: 84. Largest Rectangle in Histogram
jramaswami
"""


import collections


SItem = collections.namedtuple('SItem', ['height', 'index'])


class Solution:
    def largestRectangleArea(self, heights):
        soln = 0
        stack = []
        for i, h in enumerate(heights):
            left = i
            while stack and stack[-1].height >= h:
                left = stack[-1].index
                stack.pop()
            stack.append(SItem(h, left))

            for item in stack:
                soln = max(soln, item.height * (i - item.index + 1))
        return soln


def test_1():
    heights = [2,1,5,6,2,3]
    expected = 10
    assert Solution().largestRectangleArea(heights) == expected
