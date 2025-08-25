"""
LeetCode
498. Diagonal Traverse
August 2025 Challenge
jramaswami
"""


import dataclasses


@dataclasses.dataclass(frozen = True)
class Vector:
    row: int
    col: int

    def move(self, other):
        return Vector(self.row + other.row, self.col + other.col)

    def inbounds(self, max_row, max_col):
        return (0 <= self.row < max_row) and (0 <= self.col < max_col)


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        NE = Vector(-1, 1)
        SW = Vector(1, -1)
        E = Vector(0, 1)
        S = Vector(1, 0)

        soln = []
        posn = Vector(0, 0)
        dirn = NE
        max_row, max_col = len(mat), len(mat[0])
        stop = Vector(max_row-1, max_col-1)
        while posn != stop:
            soln.append(mat[posn.row][posn.col])
            # Move in current direction
            posn0 = posn.move(dirn)
            # If posn0 is out of bounds, change direction
            if posn0.inbounds(max_row, max_col):
                posn0 = posn.move(dirn)
            else:
                if dirn == NE:
                    # When moving NE, go E unless that will
                    # be out of bounds. Otherwise, move S.
                    posn0 = posn.move(E)
                    if not posn0.inbounds(max_row, max_col):
                        posn0 = posn.move(S)
                    dirn = SW
                elif dirn == SW:
                    # When moving SW, go S unless that will
                    # be out of bounds. Otherwise, move E.
                    posn0 = posn.move(S)
                    if not posn0.inbounds(max_row, max_col):
                        posn0 = posn.move(E)
                    dirn = NE
            posn = posn0
        soln.append(mat[posn.row][posn.col])

        return soln
