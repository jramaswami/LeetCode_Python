"""
Divide Two Integers
jramaswami
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        signs = (dividend < 0) + (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1

        if signs == 1:
            return -quotient
        return quotient


def test_1():
    assert Solution().divide(10, 3) == 3

def test_2():
    assert Solution().divide(7, -3) == -2

def test_3():
    assert Solution().divide(0, 1) == 0

def test_4():
    assert Solution().divide(1, 1) == 1
