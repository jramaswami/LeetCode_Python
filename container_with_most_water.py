"""
LeetCode :: April 2022 Challenge :: Container With Most Water
jramaswami
"""


import collections


class Solution:
    def maxArea(self, height):
        soln = 0
        H = collections.deque(height)
        while len(H) > 1:
            if H[0] < H[-1]:
                soln = max(soln, (len(H)-1) * H[0])
                H.popleft()
            else:
                soln = max(soln, (len(H)-1) * H[-1])
                H.pop()
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
