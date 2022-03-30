"""
LeetCode :: March 2022 Challenge :: 74. Search a 2D Matrix
jramaswmai
"""


class Solution:
    def searchMatrix(self, matrix, target):
        r = 0
        c = len(matrix[r]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
        return False


def test_1():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    expected = True
    assert Solution().searchMatrix(matrix, target) == expected


def test_2():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    expected = False
    assert Solution().searchMatrix(matrix, target) == expected
