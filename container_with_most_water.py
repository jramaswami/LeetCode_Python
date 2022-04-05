"""
LeetCode :: April 2022 Challenge :: Container With Most Water
jramaswami
"""


class Solution:
    def maxArea(self, height):
        soln = 0
        left = [(0, height[0])]
        for i, h in enumerate(height[1:], start=1):
            for j, k in left:
                soln = max(soln, min(h, k) * (i - j))
            if h > left[0][1]:
                left.append((i, h))
        return soln


def test_1():
    assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49


def test_2():
    assert Solution().maxArea([1,1]) == 1


def test_3():
    assert Solution().maxArea([4,3,2,1,4]) == 16


def test_4():
    assert Solution().maxArea([1,2,1]) == 2


def test_5():
    assert Solution().maxArea([1,2]) == 1
