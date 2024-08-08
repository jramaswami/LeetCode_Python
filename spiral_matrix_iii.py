"""
LeetCode
885. Spiral Matrix III
August 2024 Challenge
jramaswami
"""


import collections


Posn = collections.namedtuple('Posn', ['row', 'col'])


EAST, SOUTH, WEST, NORTH = 0, 1, 2, 3
DIRECTIONS = [Posn(0, 1), Posn(1, 0), Posn(0, -1), Posn(-1, 0)]


def move(p, d, visited):
    d0 = (d+1) % len(DIRECTIONS)
    p0 = Posn(p.row + DIRECTIONS[d0].row, p.col + DIRECTIONS[d0].col)
    if p0 in visited:
        d0 = d
        p0 = Posn(p.row + DIRECTIONS[d0].row, p.col + DIRECTIONS[d0].col)
    return p0, d0


def inbounds(p, rows, cols):
    return p.row >= 0 and p.row < rows and p.col >= 0 and p.col < cols


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        curr = Posn(rStart, cStart)
        dirn = NORTH
        soln = []
        visited = set()
        N = rows * cols
        while len(soln) < N:
            visited.add(curr)
            if inbounds(curr, rows, cols):
                soln.append(list(curr))
            curr, dirn = move(curr, dirn, visited)
        return soln