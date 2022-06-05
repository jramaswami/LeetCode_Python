"""
Leet Code :: June 2022 Challenge :: N-Queens II
jramaswami
"""


import collections


class Solution:
    def totalNQueens(self, n):
        row_taken = [False for _ in range(n)]
        neg_diag = collections.defaultdict(bool)
        pos_diag = collections.defaultdict(bool)
        soln = 0

        def peaceful(row, col):
            if row_taken[row]:
                return False
            if neg_diag[row - col]:
                return False
            if pos_diag[row + col]:
                return False
            return True

        def solve(col):
            if col >= n:
                return 1

            result = 0
            for row in range(n):
                if peaceful(row, col):
                    row_taken[row] = True
                    neg_diag[row - col] = True
                    pos_diag[row + col] = True
                    result += solve(col + 1)
                    row_taken[row] = False
                    neg_diag[row - col] = False
                    pos_diag[row + col] = False

            return result

        return solve(0)



def test_1():
    assert Solution().totalNQueens(4) == 2


def test_2():
    assert Solution().totalNQueens(1) == 1
