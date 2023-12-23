"""
LeetCode
1496. Path Crossing
December 2023 Challenge
jramaswami
"""


import collections


Vector = collections.namedtuple('Vector', ['row', 'col'])
Vector.__add__ = lambda a, b: Vector(a.row + b.row , a.col + b.col)


DIRECTIONS = {
    'N': Vector(1, 0), 'S': Vector(-1, 0),
    'E': Vector(0, 1), 'W': Vector(0, -1)
}


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        p = Vector(0, 0)
        visited.add(p)
        for d in path:
            q = p + DIRECTIONS[d]
            if q in visited:
                return True
            visited.add(q)
        return False


def test_1():
    path = "NES"
    expected = False
    assert Solution().isPathCrossing(path) == expected


def test_2():
    path = "NESWW"
    expected = True
    assert Solution().isPathCrossing(path) == expected


def test_3():
    "WA"
    path = "SS"
    expected = False
    assert Solution().isPathCrossing(path) == expected