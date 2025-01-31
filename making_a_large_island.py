"""
LeetCode
827. Making a Large Island
January 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def largestIsland(self, grid):

        def inbounds(r, c):
            """Return True if (r, c) is inside grid."""
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])

        def neighbors(r, c):
            """Return the neighbors of (r, c)."""
            offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in offsets:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield (r0, c0)

        # BFS to identify connected components and size.
        id_grid = [[0 for _ in row] for row in grid]
        sizes = collections.defaultdict(int)
        curr_id = 0
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] == 1 and id_grid[r][c] == 0:
                    curr_id += 1
                    Q = collections.deque()
                    Q.append((r, c))
                    id_grid[r][c] = curr_id
                    while Q:
                        r0, c0 = Q.popleft()
                        sizes[curr_id] += 1
                        for r1, c1 in neighbors(r0, c0):
                            if grid[r1][c1] == 1 and id_grid[r1][c1] == 0:
                                id_grid[r1][c1] = curr_id
                                Q.append((r1, c1))


        # Find all zeros and then join any adjacent islands to see what
        # sizes we can make.
        soln = 0
        if sizes:
            soln = max(sizes.values())
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] == 0:
                    neighbor_islands = set(
                            id_grid[r0][c0] for r0, c0 in neighbors(r, c)
                            if id_grid[r0][c0] > 0
                    )
                    united_size = 1 + sum(sizes[i] for i in neighbor_islands)
                    soln = max(soln, united_size)
        return soln


def test_1():
    grid = [[1,0],[0,1]]
    expected = 3
    assert Solution().largestIsland(grid) == expected


def test_2():
    grid = [[1,1],[1,0]]
    expected = 4
    assert Solution().largestIsland(grid) == expected


def test_3():
    grid = [[1,1],[1,1]]
    expected = 4
    assert Solution().largestIsland(grid) == expected
