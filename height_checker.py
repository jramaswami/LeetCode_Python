"""
LeetCode :: Array Module :: Height Checker
jramaswami
"""


class Solution:
    def heightChecker(self, heights):
        heights0 = sorted(heights)
        soln = 0
        for h, h0 in zip(heights, heights0):
            if h != h0:
                soln += 1
        return soln


def test_1():
    heights = [1, 1, 4, 2, 1, 3]
    assert Solution().heightChecker(heights) == 3


def test_2():
    heights = [5, 1, 2, 3, 4]
    assert Solution().heightChecker(heights) == 5


def test_3():
    heights = [1,2,3,4,5]
    assert Solution().heightChecker(heights) == 0



