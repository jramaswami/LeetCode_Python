"""
LeetCode
1970. Last Day Where You Can Still Cross
June 2020 Challenge
jramaswami
"""


from typing import List


class DisjointSet:

    def __init__(self, n):
        self.id = list(range(n+2))
        self.size = [1 for _ in self.id]

    def find(self, x):
        if self.id[x] != x:
            self.id[x] = self.find(self.id[x])
        return self.id[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.id[b] = a
            self.size[a] += self.size[b]


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def d1_index_to_d2(i):
            return i // col, i % col

        def d2_index_to_d1(r, c):
            return (r * col) + c

        def inbounds(r, c):
            return (
                r >= 0 and c >= 0 and
                r < row and c < col
            )

        OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def neighbors(r, c):
            for dr, dc in OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        n = row * col
        bottom_id = n
        top_id = n+1

        dsj = DisjointSet(n)

        for c in range(col):
            i = d2_index_to_d1(row-1, c)
            dsj.union(top_id, i)
            j = d2_index_to_d1(0, c)
            dsj.union(bottom_id, j)
            
        is_land = [[False for _ in range(col)] for _ in range(row)]
        for cells_index, (r, c) in enumerate(reversed(cells), start=1):
            r, c = r - 1, c - 1
            i = d2_index_to_d1(r, c)
            is_land[r][c] = True
            for r0, c0 in neighbors(r, c):
                if is_land[r0][c0]:
                    j = d2_index_to_d1(r0, c0)
                    dsj.union(i, j)
                if dsj.find(top_id) == dsj.find(bottom_id):
                    return len(cells) - cells_index


def test_1():
    row = 2
    col = 2
    cells = [[1,1],[2,1],[1,2],[2,2]]
    expected = 2
    assert Solution().latestDayToCross(row, col, cells) == expected


def test_2():
    row = 2
    col = 2
    cells = [[1,1],[1,2],[2,1],[2,2]]
    expected = 1
    assert Solution().latestDayToCross(row, col, cells) == expected


def test_3():
    row = 3
    col = 3
    cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
    expected = 3
    assert Solution().latestDayToCross(row, col, cells) == expected
