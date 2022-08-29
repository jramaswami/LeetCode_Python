"""
LeetCode :: August 2022 Challenge :: 200. Number of Islands
jramaswami
"""


import collections


class Solution:

    def numIslands(self, grid):
        def inbounds(r, c):
            return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])

        offsets = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def neighbors(r, c):
            for dr, dc in offsets:
                r0, c0 = r+dr, c+dc
                if inbounds(r0, c0) and grid[r0][c0] == '1':
                    yield r0, c0

        visited = [[False for _ in row] for row in grid]
        def bfs(r, c):
            visited[r][c] = True
            queue = collections.deque()
            queue.append((r, c))
            while queue:
                r0, c0 = queue.popleft()
                for r1, c1 in neighbors(r0, c0):
                    if not visited[r1][c1]:
                        visited[r1][c1] = True
                        queue.append((r1, c1))

        soln = 0
        for r, row in enumerate(grid):
            for c, _ in enumerate(row):
                if grid[r][c] == '1' and not visited[r][c]:
                    bfs(r, c)
                    soln += 1
        return soln


def test_1():
    grid = [ ["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"] ]
    expected = 1
    assert Solution().numIslands(grid) == expected


def test_2():
    grid = [ ["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"] ]
    expected = 3
    assert Solution().numIslands(grid) == expected
