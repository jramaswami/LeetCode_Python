"""
LeetCode
1277. Count Square Submatrices with All Ones
October 2024 Challenge
jramaswami
"""


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        prefix = [[0 for _ in row] for row in matrix]
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                prefix[r][c] = matrix[r][c]
                if r > 0:
                    prefix[r][c] += prefix[r-1][c]
                if c > 0:
                    prefix[r][c] += prefix[r][c-1]
                if r > 0 and c > 0:
                    prefix[r][c] -= prefix[r-1][c-1]

        def get(r, c):
            if r < 0 or c < 0:
                return 0
            return prefix[r][c]

        soln = 0
        for r1 in range(len(matrix)):
            for c1 in range(len(matrix[r1])):
                for n in range(len(matrix)):
                    y = pow(n+1,2)
                    if r1 + n >= len(matrix) or c1 + n >= len(matrix[r]):
                        break
                    r2, c2 = r1 + n, c1 + n
                    x = get(r2, c2) - get(r1-1, c2) - get(r2, c1-1) + get(r1-1, c1-1)
                    if x == y:
                        soln += 1
        return soln
