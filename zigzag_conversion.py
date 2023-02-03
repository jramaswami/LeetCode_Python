"""
LeetCode
6. Zigzag Conversion
February 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        i = r = c = 0
        soln = [[""] for _ in range(numRows)]
        while i < len(s):
            # Row wise
            for _ in range(numRows):
                if i < len(s):
                    if c >= len(soln[r]):
                        for y in range(numRows):
                            soln[r].append("")
                    soln[r][c] = s[i]
                    i += 1
                r += 1
            r -= 2
            c += 1
            # Col wise
            for _ in range(numRows-2):
                if i < len(s):
                    if c >= len(soln[r]):
                        for y in range(numRows):
                            soln[r].append("")
                    soln[r][c] = s[i]
                    i += 1
                r -= 1
                c += 1

        return "".join("".join(row) for row in soln)


def test_1():
    s = "PAYPALISHIRING"
    numRows = 3
    expected = "PAHNAPLSIIGYIR"
    assert Solution().convert(s, numRows) == expected


def test_2():
    s = "PAYPALISHIRING"
    numRows = 4
    expected = "PINALSIGYAHRPI"
    assert Solution().convert(s, numRows) == expected


def test_3():
    s = "A"
    numRows = 1
    expected = "A"
    assert Solution().convert(s, numRows) == expected


def test_4():
    "RTE"
    s = "ABC"
    numRows = 1
    expected = "ABC"
    assert Solution().convert(s, numRows) == expected