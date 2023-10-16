"""
LeetCode
119. Pascal's Triangle II
October 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        prevRow = [1,1]
        nextRow = [1]
        for i in range(2, rowIndex+1):
            for i, _ in enumerate(prevRow[:-1]):
                nextRow.append(prevRow[i]+prevRow[i+1])
            nextRow.append(1)
            prevRow, nextRow = nextRow, [1]

        return prevRow


def test_1():
    rowIndex = 3
    expected = [1,3,3,1]
    assert Solution().getRow(rowIndex) == expected


def test_2():
    rowIndex = 0
    expected = [1]
    assert Solution().getRow(rowIndex) == expected


def test_3():
    rowIndex = 1
    expected = [1,1]
    assert Solution().getRow(rowIndex) == expected


def test_4():
    rowIndex = 7
    expected = [1,7,21,35,35,21,7,1]
    assert Solution().getRow(rowIndex) == expected