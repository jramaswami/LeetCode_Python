"""
LeetCode :: March 2021 Challenge :: Integer to Roman
jramaswami
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        romans = []
        while num >= 1000:
            romans.append("M")
            num -= 1000
        
        while num >= 500:
            if num >= 900:
                romans.append("CM")
                num -= 900
            else:
                romans.append("D")
                num -= 500

        while num >= 100:
            if num >= 400:
                romans.append("CD")
                num -= 400
            else:
                romans.append("C")
                num -= 100

        while num >= 50:
            if num >= 90:
                romans.append("XC")
                num -= 90
            else:
                romans.append("L")
                num -= 50

        while num >= 10:
            if num >= 40:
                romans.append("XL")
                num -= 40
            else:
                romans.append("X")
                num -= 10

        while num >= 5:
            if num >= 9:
                romans.append("IX")
                num -= 9
            else:
                romans.append("V")
                num -= 5

        while num > 0:
            if num >= 4:
                romans.append("IV")
                num -= 4
            else:
                romans.append("I")
                num -= 1

        return "".join(romans)


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

