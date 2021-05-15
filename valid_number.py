"""
LeetCode :: May 2021 Challenge :: Valid Number
jramaswami
"""
from typing import *


class Solution:
    def isNumber(self, s: str) -> bool:

        def validInteger(s):
            # Optional sign
            if s[0] in ['+', '-']:
                s = s[1:]
            if not s:
                return False
            return all(c.isdigit() for c in s)

        def validDecimal(s):
            try:
                i = s.index('.')
                whole, fraction = s[:i], s[i+1:]
                if fraction and not fraction[0].isdigit():
                    # Fraction cannot have sign.
                    return False
                if whole and whole[0] in ['-', '+']:
                    whole = whole[1:]
                if not whole and not fraction:
                    # .
                    return False
                if whole:
                    #123.123
                    if fraction:
                        return validInteger(whole) and validInteger(fraction)
                    return validInteger(whole)
                # .123
                return validInteger(fraction)
            except ValueError:
                return validInteger(s)

        s0 = s.lower()
        try:
            i = s0.index('e')
            mantissa, exponent = s[:i], s[i+1:]
            if not mantissa or not exponent:
                # 123e or e123
                return False
            return validDecimal(mantissa) and validInteger(exponent)
        except ValueError:
            return validDecimal(s)


def test_1():
    s = "0"
    assert Solution().isNumber(s) == True

def test_2():
    s = "e"
    assert Solution().isNumber(s) == False

def test_3():
    s = "."
    assert Solution().isNumber(s) == False

def test_4():
    s = ".1"
    assert Solution().isNumber(s) == True

def test_5():
    """WA"""
    s = "-1"
    assert Solution().isNumber(s) == True

def test_6():
    """WA"""
    s = "3."
    assert Solution().isNumber(s) == True

def test_7():
    """WA"""
    s = "4e+"
    assert Solution().isNumber(s) == False

def test_8():
    """WA"""
    s = ".-4"
    assert Solution().isNumber(s) == False

def test_9():
    """WA"""
    s = "+.8"
    assert Solution().isNumber(s) == True
