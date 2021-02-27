"""
Divide Two Integers
jramaswami
"""
BIT_LIMIT = 32


def most_significant_bit(n):
    """Return the index of the most significat bit."""
    msb = 0
    for b in range(BIT_LIMIT):
        mask = (1 << b)
        if mask & n:
            msb = b
    return msb


def is_bit_set(n, bit):
    """Return true if bit is set."""
    mask = (1 << bit)
    return (mask & n)


def set_bit(n, bit):
    """Set bit at given position on."""
    mask = (1 << bit)
    return (n | mask)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        signs = (dividend < 0) + (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        # Find the most significant bit in dividend.
        msb = most_significant_bit(dividend)
        
        quotient = 0
        working = 0
        for b in range(msb, -1, -1):
            # Shift working 1 place left
            working = working << 1
            # Put in the bit from dividend
            if is_bit_set(dividend, b):
                working |= 1

            # If our working number is more than the divsor, subtract divsor
            # from quotient and set the bit at this position.
            if working >= divisor:
                working -= divisor
                quotient = set_bit(quotient, b)

        max_quotient = (1 << 31) - 1
        if signs == 1:
            quotient = -quotient
        return min(max_quotient, quotient)


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
