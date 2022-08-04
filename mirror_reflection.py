"""
LeetCode :: August 2022 Challenge :: Mirror Reflection
jramaswami

2------1
|      | a
|      |
.------0
   b

REF: https://brilliant.org/courses/basic-number-theory/gcd-and-lcm-2/billiard-tables-revisited-ii/1/
"""


import math


class Solution:
    def mirrorReflection(self, b: int, a: int) -> int:
        g = math.gcd(a, b)
        bounces_top_bottom = (a // g) - 1
        bounces_left_right = (b // g) - 1
        if bounces_top_bottom % 2 == 0:
            if bounces_left_right % 2 == 1:
                return 2
            else:
                return 1
        elif bounces_top_bottom % 2 == 1:
            if bounces_left_right % 2 == 1:
                # This is not supposed to happen.
                pass
            else:
                return 0


def test_1():
    a, b = 2, 1
    expected = 2
    assert Solution().mirrorReflection(a, b) == expected


def test_2():
    a, b = 3, 1
    expected = 1
    assert Solution().mirrorReflection(a, b) == expected
