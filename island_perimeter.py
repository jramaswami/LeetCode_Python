"""
LeetCode :: October 2021 Challenge :: 463. Island Perimeter
jramaswami
"""


from collections import deque


class Solution:
    def islandPerimeter(self, grid):

        def inbounds(r, c):
            """Return True if row and column are inside grid."""
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])

        def neighbors(r, c):
            """Generator for neighbors."""
            offsets = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for dr, dc in offsets:
                r0, c0 = r + dr, c + dc
                yield (r0, c0)

        def is_water(r, c):
            """Return True if cell is water."""
            if inbounds(r, c):
                return grid[r][c] == 0
            return True

        def find_land():
            """Find any piece of land."""
            for r, row in enumerate(grid):
                for c, val in enumerate(row):
                    if val == 1:
                        return (r, c)

        root = find_land()

        # BFS to find all land.  The edge of the land is any side that
        # is adjacent to water so the perimeter is the sum of all the
        # adjacent neighbors that are water.
        soln = 0
        visited = set()
        visited.add(root)
        queue = deque()
        queue.append(root)
        while queue:
            r, c = queue.popleft()
            for r0, c0 in neighbors(r, c):
                    if is_water(r0, c0):
                        # A water cell adjacent to a land cell, add to solution.
                        soln += 1
                    else:
                        # A land cell, add it to the queue if not visited.
                        if (r0, c0) not in visited:
                            visited.add((r0, c0))
                            queue.append((r0, c0))
        return soln


def test_1():
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    expected = 16
    assert Solution().islandPerimeter(grid) == expected


def test_2():
    grid = [[1]]
    expected = 4
    assert Solution().islandPerimeter(grid) == expected


def test_3():
    grid = [[1,0]]
    expected = 4
    assert Solution().islandPerimeter(grid) == expected


