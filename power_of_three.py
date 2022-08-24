"""
Leet Code :: August 2022 Challenge :: Power of Three
jramaswami
"""


import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and math.log(n, 3).is_integer()


def test_1():
    "WA"
    assert Solution().isPowerOfThree(243) == True