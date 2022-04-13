"""
LeetCode :: April 2022 Challenge :: 59. Spiral Matrix II
jramaswami
"""


class Solution:

    def generateMatrix(self, n):
        offsets = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def inbounds(r, c):
            return r >= 0 and r < n and c >= 0 and c < n

        def move(r, c, curr_dirn):
            dr, dc = offsets[curr_dirn]
            r0, c0 = r + dr, c + dc
            if inbounds(r0, c0) and matrix[r0][c0] == 0:
                return r0, c0
            return None, None

        def turn(curr_dirn):
            return (curr_dirn + 1) % len(offsets)

        curr_dirn = 0
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        r, c = 0, -1
        for i in range(n * n):
            r0, c0 = move(r, c, curr_dirn)
            while r0 is None:
                curr_dirn = turn(curr_dirn)
                r0, c0 = move(r, c, curr_dirn)
            r, c = r0, c0
            matrix[r][c] = i + 1
        return matrix


def test_1():
    n = 3
    expected = [[1,2,3],[8,9,4],[7,6,5]]
    assert Solution().generateMatrix(n) == expected


def test_2():
    n = 1
    expected = [[1]]
    assert Solution().generateMatrix(n) == expected
