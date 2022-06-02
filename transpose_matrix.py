"""
LeetCode :: June 2022 Challenge :: 867. Transpose Matrix
jramaswami
"""


class Solution:

    def transpose(self, matrix):
        height = len(matrix)
        width = len(matrix[0])
        result = [[0 for _ in range(height)] for _ in range(width)]

        for result_c, row in enumerate(matrix):
            for result_r, val in enumerate(row):
                result[result_r][result_c] = val
        return result


def test_1():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    expected = [[1,4,7],[2,5,8],[3,6,9]]
    assert Solution().transpose(matrix) == expected


def test_2():
    matrix = [[1,2,3],[4,5,6]]
    expected = [[1,4],[2,5],[3,6]]
    assert Solution().transpose(matrix) == expected
