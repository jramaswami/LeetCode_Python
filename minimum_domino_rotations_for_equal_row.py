"""
LeetCode :: March 2022 Challenge :: 1007. Minimum Domino Rotations For Equal Row
jramaswami
"""


import math


class Solution:
    def minDominoRotations(self, tops, bottoms):
        # Top
        soln = math.inf
        value = tops[0]
        i = 1
        cost = 0
        while i < len(tops):
            t = tops[i]
            b = bottoms[i]
            if t == value:
                i += 1
            elif b == value:
                i += 1
                cost += 1
            else:
                break
        if i == len(tops):
            soln = min(soln, cost, len(tops) - cost)

        # Bottom
        value = bottoms[0]
        i = 1
        cost = 0
        while i < len(bottoms):
            t = tops[i]
            b = bottoms[i]
            if b == value:
                i += 1
            elif t == value:
                i += 1
                cost += 1
            else:
                break
        if i == len(bottoms):
            soln = min(soln, cost, len(bottoms) - cost)

        return (-1 if soln == math.inf else soln)


def test_1():
    tops = [2,1,2,4,2,2]
    bottoms = [5,2,6,2,3,2]
    expected = 2
    assert Solution().minDominoRotations(tops, bottoms) == expected


def test_2():
    tops = [3,5,1,2,3]
    bottoms = [3,6,3,3,4]
    expected = -1
    assert Solution().minDominoRotations(tops, bottoms) == expected


def test_3():
    tops =    [3, 1, 1, 1, 1, 1]
    bottoms = [1, 1, 3, 4, 5, 6]
    expected = 1
    assert Solution().minDominoRotations(tops, bottoms) == expected
