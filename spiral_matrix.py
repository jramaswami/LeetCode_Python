"""
LeetCode :: September 2021 Challenge :: Spiral Matrix
jramaswami
"""

from collections import namedtuple


Posn = namedtuple('Posn', ['row', 'col'])
Dirn = namedtuple('Dirn', ['row_offset', 'col_offset'])


class Solution:

    def spiralOrder(self, matrix):
        # Corner case of empty matrix.
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        directions = (Dirn(0, 1), Dirn(1, 0), Dirn(-1, 0), Dirn(0, -1))
        current_direction = 0
        cell_count = len(matrix) * len(matrix[0])

        def inbounds(posn):
            """Return True if posn is inbounds."""
            return (posn.row >= 0 and posn.row < len(matrix) and
                    posn.col >= 0 and posn.col < len(matrix[0]))

        def move(posn, current_direction):
            """Return the next position given the current direction."""
            offset = directions[current_direction]
            return Posn(posn.row + offset.row_offset,
                        posn.col + offset.col_offset)

        visited = [[False for _ in row] for row in matrix]
        soln = []
        posn = Posn(0, 0)
        current_direction = 0
        while 1:
            if not visited[posn.row][posn.col]:
                visited[posn.row][posn.col] = True
                soln.append(matrix[posn.row][posn.col])

            # If we have visited all the cells, stop.
            if len(soln) == cell_count:
                break

            # Try to move forward in current direction.
            next_posn = move(posn, current_direction)
            if inbounds(next_posn) and not visited[next_posn.row][next_posn.col]:
                # Move.
                posn = next_posn
            else:
                # Turn.
                current_direction = (current_direction + 1) % len(directions)

        return soln


def test_1():
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    expected = [1,2,3,4,8,12,11,10,9,5,6,7]
    assert Solution().spiralOrder(matrix) == expected


def test_2():
    matrix = [ [6, 9, 8], [1, 8, 0], [5, 1, 2], [8, 0, 3], [1, 6, 4], [8, 8, 10] ]
    expected = [6, 9, 8, 0, 2, 3, 4, 10, 8, 8, 1, 8, 5, 1, 8, 1, 0, 6]
    assert Solution().spiralOrder(matrix) == expected


def test_3():
    matrix = [[]]
    expected = []
    assert Solution().spiralOrder(matrix) == expected


def test_4():
    matrix = []
    expected = []
    assert Solution().spiralOrder(matrix) == expected


def test_5():
    matrix = [[1,2,3,4,5]]
    expected = [1,2,3,4,5]
    assert Solution().spiralOrder(matrix) == expected


def test_6():
    matrix = [[1],[2],[3],[4],[5]]
    expected = [1,2,3,4,5]
    assert Solution().spiralOrder(matrix) == expected
