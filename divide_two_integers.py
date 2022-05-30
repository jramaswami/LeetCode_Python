"""
Divide Two Integers
jramaswami
"""


class Solution:
    def divide(self, dividend, divisor):

        def bit_is_set(num, bit):
            mask = (1 << bit)
            return (num & mask)

        BIT_LIMIT = 31
        LOWER_LIMIT = -pow(2, 31)
        UPPER_LIMIT = pow(2, 31) - 1

        result_is_negative = False
        if dividend < 0 and divisor >= 0:
            result_is_negative = True
        elif dividend >= 0 and divisor < 0:
            result_is_negative = True
        dividend, divisor = abs(dividend), abs(divisor)

        x = 0
        result = 0
        for b in range(BIT_LIMIT, -1, -1):
            result = result << 1
            x = x << 1

            if bit_is_set(dividend, b):
                x |= 1

            if x >= divisor:
                result |= 1
                x -= divisor

        if result_is_negative:
            return max(-result, LOWER_LIMIT)
        return min(result, UPPER_LIMIT)


def test_1():
    assert Solution().divide(10, 3) == 3

def test_2():
    assert Solution().divide(7, -3) == -2

def test_3():
    assert Solution().divide(0, 1) == 0

def test_4():
    assert Solution().divide(1, 1) == 1

def test_5():
    assert Solution().divide(-2147483648, -1) == 2147483647
