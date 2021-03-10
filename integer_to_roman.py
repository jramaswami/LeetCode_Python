"""
LeetCode :: March 2021 Challenge :: Integer to Roman
jramaswami
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = [1,   4,    5,   9,   10,  40,   50,  90,   100, 400,  500, 900,  1000]
        romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        soln = []
        while num > 0:
            if num >= numbers[-1]:
                num -= numbers[-1]
                soln.append(romans[-1])
            else:
                numbers.pop()
                romans.pop()
        return "".join(soln)


def test_1():
    assert Solution().intToRoman(3) == "III"

def test_2():
    assert Solution().intToRoman(4) == "IV"

def test_3():
    assert Solution().intToRoman(9) == "IX"

def test_4():
    assert Solution().intToRoman(58) == "LVIII"

def test_5():
    assert Solution().intToRoman(1994) == "MCMXCIV"

