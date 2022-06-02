"""
LeetCode :: Grind 75 :: Flood Fill
jramaswami
"""


from typing import *
import collections


class Solution:

    OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # Do not mutate original
        image0 = [list(row) for row in image]

        def inbounds(r, c):
            return r >= 0 and r < len(image0) and c >= 0 and c < len(image0[r])

        def neighbors(r, c):
            for dr, dc in Solution.OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        fromColor = image0[sr][sc]
        image0[sr][sc] = newColor
        queue = collections.deque([(sr, sc)])
        while queue:
            r, c = queue.popleft()
            for r0, c0 in neighbors(r, c):
                if image0[r0][c0] == fromColor:
                    image0[r0][c0] = newColor
                    queue.append((r0, c0))
        return image0


def test_1():
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    expected = [[2,2,2],[2,2,0],[2,0,1]]
    assert Solution().floodFill(image, sr, sc, newColor) == expected


def test_2():
    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    newColor = 2
    expected = [[2,2,2],[2,2,2]]
    assert Solution().floodFill(image, sr, sc, newColor) == expected


def test_3():
    "TLE"
    image = [[0,0,0],[0,1,1]]
    sr = 1
    sc = 1
    newColor = 1
    expected = [[2,2,2],[2,2,2]]
    assert Solution().floodFill(image, sr, sc, newColor) == expected
