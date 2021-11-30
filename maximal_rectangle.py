"""
LeetCode :: November 2021 Challenge:: 85. Maximal Rectangle
jramaswami
"""


import collections


SItem = collections.namedtuple('SItem', ['idx', 'ht'])


class Solution:

    def maximalRectangle(self, matrix):
        # Corner case:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        # The height of the column at (r, c).
        heights = [[0 for _ in row] for row in matrix]
        for c, _ in enumerate(matrix[0]):
            for r, _ in enumerate(matrix):
                if r == 0:
                    if matrix[r][c] == '1':
                        heights[r][c] = 1
                else:
                    if matrix[r][c] == '1':
                        heights[r][c] = 1 + heights[r-1][c]

        soln = 0
        # For each row, find the maximum under the histogram.
        for row in heights:
            # Stack will always hold the leftmost index for a given height.
            # All heights are in ascending order.
            stack = []
            for c, ht in enumerate(row):
                # Find the leftmost item with a height greater than ht.
                left = c
                while stack and stack[-1].ht >= ht:
                    left = stack[-1].idx
                    stack.pop()
                stack.append(SItem(left, ht))

                T = max(s.ht * (1 + c - s.idx) for s in stack)
                soln = max(soln, T)
        return soln


def test_1():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    expected = 6
    assert Solution().maximalRectangle(matrix) == expected



def test_2():
    matrix = []
    expected = 0
    assert Solution().maximalRectangle(matrix) == expected


def test_3():
    matrix = [["0"]]
    expected = 0
    assert Solution().maximalRectangle(matrix) == expected


def test_4():
    matrix = [["1"]]
    expected = 1
    assert Solution().maximalRectangle(matrix) == expected
