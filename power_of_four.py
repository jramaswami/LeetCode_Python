"""
LeetCode :: August 2022 Challenge :: 342. Power of Four
jramaswami
"""


import math


class Solution:

    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return math.log(abs(n), 4).is_integer()


def test_1():
    assert Solution().isPowerOfFour(4) == True


def test_2():
    assert Solution().isPowerOfFour(5) == False


def test_3():
    assert Solution().isPowerOfFour(1) == True


def test_4():
    "WA"
    assert Solution().isPowerOfFour(-64) == False