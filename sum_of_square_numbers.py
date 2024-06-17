"""
LeetCode
633. Sum of Square Numbers
June 2024 Challenge
jramaswmai
"""


import bisect


def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        squares = []
        x = 0
        while x * x <= c:
            squares.append(x * x)
            x += 1

        for sq in squares:
            y = c - sq
            try:
                i = index(squares, y)
                return True
            except ValueError:
                pass

        return False


def test_1():
    c = 5
    expected = True
    assert Solution().judgeSquareSum(c) == expected


def test_2():
    c = 3
    expected = False
    assert Solution().judgeSquareSum(c) == expected