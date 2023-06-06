"""
LeetCode
1502. Can Make Arithmetic Progression From Sequence
June 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        delta = arr[0] - arr[1]
        for a, b in zip(arr[:-1], arr[1:]):
            if a - b != delta:
                return False
        return True


def test_1():
    arr = [3,5,1]
    expected = True
    assert Solution().canMakeArithmeticProgression(arr) == expected


def test_2():
    arr = [1,2,4]
    expected = False
    assert Solution().canMakeArithmeticProgression(arr) == expected
