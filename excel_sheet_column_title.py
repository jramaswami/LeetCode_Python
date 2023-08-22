"""
LeetCode
168. Excel Sheet Column Title
August 2023 Challenge
jramaswami

REF: https://stackoverflow.com/questions/181596/how-to-convert-a-column-number-e-g-127-into-an-excel-column-e-g-aa
"""


import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        soln = []
        while columnNumber:
            i = (columnNumber - 1) % 26
            t = string.ascii_uppercase[i]
            soln.append(t)
            columnNumber = (columnNumber - i) // 26
        return "".join(soln[::-1])


def test_1():
    assert Solution().convertToTitle(1) == 'A'


def test_2():
    assert Solution().convertToTitle(28) == 'AB'


def test_3():
    assert Solution().convertToTitle(701) == 'ZY'


def test_4():
    assert Solution().convertToTitle(2147483647) == 'FXSHRXW'


def test_5():
    assert Solution().convertToTitle(52) == "AZ"