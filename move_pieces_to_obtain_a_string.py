"""
LeetCode
2337. Move Pieces to Obtain a String
December 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start0 = collections.deque((i, x) for i, x in enumerate(start) if x in 'LR')
        target0 = collections.deque((i, x) for i, x in enumerate(target) if x in 'LR')

        for s, t in zip(start0, target0):
            if s[1] != t[1]:
                return False
            if s[1] == 'L' and t[0] > s[0]:
                return False
            if s[1] == 'R' and t[0] < s[0]:
                return False
        return True


def test1():
    start = "_L__R__R_"
    target = "L______RR"
    expected = True
    assert Solution().canChange(start, target) == expected


def test_2():
    start = "R_L_"
    target = "__LR"
    expected = False
    assert Solution().canChange(start, target) == expected


def test_3():
    start = "_R"
    target = "R_"
    expected = False
    assert Solution().canChange(start, target) == expected


def test_4():
    start = "R_L__R__R_"
    target = "_L______RR"
    expected = False
    assert Solution().canChange(start, target) == expected


def test_5():
    start = "R__L"
    target = "_LR_"
    expected = False
    assert Solution().canChange(start, target) == expected


def test_6():
    "WA"
    start = "_L__R__R_L"
    target = "L______RR_"
    expected = False
    assert Solution().canChange(start, target) == expected