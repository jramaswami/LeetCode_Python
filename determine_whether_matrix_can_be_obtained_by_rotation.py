"""
LeetCode
1886. Determine Whether Matrix Can Be Obtained By Rotation
March 2026 Challenge
jramaswami
"""


class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        def rotate(m):
            n = len(m)
            m0 = [[0 for _ in row] for row in m]
            for r, row in enumerate(m):
                for c, _ in enumerate(row):
                    m0[c][n-r-1] = m[r][c]
            return m0

        def equal(m1, m2):
            return all(r1 == r2 for r1, r2 in zip(m1, m2))

        for _ in range(4):
            if equal(mat, target):
                return True
            mat = rotate(mat)
        return False