"""
LeetCode :: September 2021 Challenge :: Erect The Fence
jramaswami

REF: https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain#Python
"""

from collections import namedtuple
from itertools import chain


Point = namedtuple('Point', ['x', 'y'])


def cross(O, A, B):
    """
    2D cross product of OA and OB vectors.
    Returns a positive value for a counter-clockwise turn, a negative value
    for a clockwise turn, and a zero if the points are collinear.
    """
    return (A.x - O.x) * (B.y - O.y) - (A.y - O.y) * (B.x - O.x)


class Solution:

    def outerTrees(self, trees):
        """Monotone chain algorithm to find the convex hull."""

        # Convert to points.
        points = [Point(*t) for t in trees]

        # Sort the points by x then y (which is how the named tuple will sort).
        points.sort()

        # Build lower hull
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # Build upper hull
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        return [[p.x, p.y] for p in set(chain(upper, lower))]


def test_1():
    points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    expected = [[1,1],[2,0],[3,3],[2,4],[4,2]]
    result = Solution().outerTrees(points)
    assert len(expected) == len(result)
    assert all(p in result for p in expected)
    assert all(p in expected for p in result)


def test_2():
    points = [[1,2],[2,2],[4,2]]
    expected = [[1,2],[2,2],[4,2]]
    result = Solution().outerTrees(points)
    assert len(expected) == len(result)
    assert all(p in result for p in expected)
    assert all(p in expected for p in result)


def test_3():
    points = [[80, 1], [33, 45], [70, 73], [20, 84], [63, 43], [92, 88],
              [94, 30], [97, 1], [48, 93], [17, 5], [94, 69], [20, 95],
              [69, 24], [60, 21], [77, 37], [9, 92], [42, 25], [64, 0],
              [13, 83], [53, 0], [7, 94], [93, 8], [73, 39], [17, 16],
              [3, 44], [19, 34], [34, 16], [39, 39], [54, 92], [46, 63],
              [89, 95], [90, 5], [52, 85], [13, 78], [55, 56], [22, 16],
              [82, 46], [17, 75], [22, 89], [52, 5], [75, 25], [9, 37],
              [37, 62], [95, 24], [76, 53], [92, 71], [48, 46], [70, 22],
              [15, 61], [2, 6], [52, 89], [76, 83], [79, 82], [20, 14],
              [2, 97], [92, 64], [2, 63], [20, 62], [57, 99], [53, 86],
              [36, 15], [87, 33], [41, 66], [90, 50], [75, 77], [91, 97],
              [19, 35], [57, 46], [24, 61], [27, 78], [89, 96], [88, 82],
              [28, 95], [22, 8], [61, 46], [87, 74], [15, 33], [75, 63],
              [76, 64], [2, 69], [83, 97], [2, 23], [24, 20], [31, 13],
              [21, 12], [38, 37], [15, 44], [28, 8], [18, 40], [65, 57],
              [33, 4], [30, 32], [69, 36], [4, 44], [87, 69], [89, 66],
              [69, 63], [50, 4], [50, 77]]

    expected = [[92,88],[57,99],[97,1],[53,0],[2,97],[2,69],[64,0],[91,97],
                [2,23],[2,63],[2,6],[94,69]]
    result = Solution().outerTrees(points)
    assert len(expected) == len(result)
    assert all(p in result for p in expected)
    assert all(p in expected for p in result)


def test_4():
    points = [[80, 1], [33, 45], [70, 73]]
    expected = [[80, 1], [33, 45], [70, 73]]
    result = Solution().outerTrees(points)
    assert len(expected) == len(result)
    assert all(p in result for p in expected)
    assert all(p in expected for p in result)


def test_5():
    points = [[80, 1], [33, 45]]
    expected = [[80, 1], [33, 45]]
    result = Solution().outerTrees(points)
    assert len(expected) == len(result)
    assert all(p in result for p in expected)
    assert all(p in expected for p in result)


def test_6():
    points = [[80, 1]]
    expected = [[80, 1]]
    result = Solution().outerTrees(points)
    assert len(expected) == len(result)
    assert all(p in result for p in expected)
    assert all(p in expected for p in result)
