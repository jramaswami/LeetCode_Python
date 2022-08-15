"""
LeetCode :: August 2022 Challenge :: Roman to Integer
jramaswami
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = (
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V",), (4, "IV"), (1, "I")
        )
        soln = 0
        i = 0
        for v, t in symbols:
            while s[i:i+len(t)] == t:
                soln += v
                i += len(t)
        return soln


def test_1():
    assert Solution().romanToInt("III") == 3


def test_2():
    assert Solution().romanToInt("IV") == 4


def test_3():
    assert Solution().romanToInt("IX") == 9


def test_4():
    assert Solution().romanToInt("LVIII") == 58


def test_5():
    assert Solution().romanToInt("MCMXCIV") == 1994