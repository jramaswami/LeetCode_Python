"""
LeetCode :: July 2021 Challenge :: Kth Smallest Element in a Sorted Matrix
"""

from math import inf


class Solution:
    def kthSmallest(self, matrix, k):
        # Traverse by rows.
        curr_val = 0
        indexes = [(r, 0, row[0]) for r, row in enumerate(matrix)]
        for _ in range(k):
            # Pick row with smallest value
            r, c, curr_val = min(indexes, key=lambda t: t[2])
            if c + 1 >= len(matrix[r]):
                indexes[r] = (r, c + 1, inf)
            else:
                indexes[r] = (r, c + 1, matrix[r][c+1])
        return curr_val


def test_1():
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    expected = 13
    assert Solution().kthSmallest(matrix, k) == expected


def test_2():
    matrix = [[-5]]
    k = 1
    expected = -5
    assert Solution().kthSmallest(matrix, k) == expected

