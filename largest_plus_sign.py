"""
LeetCode :: September 2021 Challenge :: Largest Plus Sign
jramaswami
"""


class Solution:
    def orderOfLargestPlusSign(self, dim, mines):
        # Build matrix.
        matrix = [[1 for _ in range(dim)] for _ in range(dim)]
        # Set mines.
        for r, c in mines:
            matrix[r][c] = 0

        # Row-wise prefix sum.
        l2r = [[0 for _ in row] for row in matrix]
        for r, row in enumerate(matrix):
            curr = 0
            for c, val in enumerate(row):
                if val == 0:
                    curr = 0
                else:
                    curr += 1
                l2r[r][c] = curr

        # Row-wise suffix sum.
        r2l = [[0 for _ in row] for row in matrix]
        for r, row in enumerate(matrix):
            curr = 0
            for dc, val in enumerate(reversed(row)):
                c = len(row) - 1 - dc
                if val == 0:
                    curr = 0
                else:
                    curr += 1
                r2l[r][c] = curr

        # Column-wise prefix sum.
        u2d = [[0 for _ in row] for row in matrix]
        for c, _ in enumerate(matrix[0]):
            curr = 0
            for r, _ in enumerate(matrix):
                if matrix[r][c] == 0:
                    curr = 0
                else:
                    curr += 1
                u2d[r][c] = curr

        # Column-wise suffix sum.
        d2u = [[0 for _ in row] for row in matrix]
        for c, _ in enumerate(matrix[0]):
            curr = 0
            for dr, _ in enumerate(matrix):
                r = len(matrix) - 1 - dr
                if matrix[r][c] == 0:
                    curr = 0
                else:
                    curr += 1
                d2u[r][c] = curr

        soln = 0
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                plus = min(l2r[r][c], r2l[r][c], u2d[r][c], d2u[r][c])
                # print(f"{r=}, {c=}, {plus=} {l2r[r][c]=} {r2l[r][c]=} {u2d[r][c]=} {d2u[r][c]=}")
                soln = max(soln, plus)
        return soln



def test_1():
    dim = 5
    mines = [[4,2]]
    assert Solution().orderOfLargestPlusSign(dim, mines) == 2


def test_2():
    dim = 1
    mines = [[0,0]]
    assert Solution().orderOfLargestPlusSign(dim, mines) == 0


def test_3():
    dim = 5
    mines = []
    assert Solution().orderOfLargestPlusSign(dim, mines) == 3
