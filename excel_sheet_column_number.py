"""
LeetCode :: February 2022 Challenge :: 171. Excel Sheet Column Number
jramaswami
"""


class Solution:

    def titleToNumber(self, columnTitle):

        def l2n(ltr):
            return 1 + ord(ltr) - ord('A')

        soln = 0
        for i, t in enumerate(columnTitle[::-1]):
            soln += pow(26, i) * l2n(t)
        return soln


def test_1():
    columnTitle = "A"
    expected = 1
    assert Solution().titleToNumber(columnTitle) == expected


def test_2():
    columnTitle = "AB"
    expected = 28
    assert Solution().titleToNumber(columnTitle) == expected


def test_3():
    columnTitle = "ZY"
    expected = 701
    assert Solution().titleToNumber(columnTitle) == expected
