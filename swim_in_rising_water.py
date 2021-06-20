"""
LeetCode :: June 2021 Challenge :: Swim in Rising Water
jramaswami
"""


from collections import deque
from math import inf


class Solution:
    def swimInWater(self, grid):

        def inbounds(r, c):
            """Return True if r, c is inside the grid."""
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])

        def neighbors(r, c):
            """Return the neighbors of r, c."""
            offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in offsets:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield (r0, c0)

        for row in grid:
            print(row)

        dp = [[inf for val in row] for row in grid]
        visited = [[False for _ in row] for row in grid]
        queue = deque([(grid[0][0], 0, 0)])
        visited[0][0] = True
        while queue:
            hw, r, c = queue.popleft()
            print(hw, r, c)
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return hw
            # From here, swimmer should go to the minimum neighbor
            # that has not been visited.
            ns = [(grid[r0][c0], r0, c0) for r0, c0 in neighbors(r, c) if not visited[r0][c0]]
            if ns:
                hw0, r0, c0 = min(ns)
                print(f"({hw}, {r}, {c}) -> ({hw0}, {r0}, {c0})")
                hw0 = max(hw, hw0)
                queue.append((hw0, r0, c0))
                visited[r0][c0] = True



def test_1():
    grid = [[0,2],[1,3]]
    expected = 3
    assert Solution().swimInWater(grid) == expected


def test_2():
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    expected = 16
    assert Solution().swimInWater(grid) == expected


def test_3():
    """WA"""
    grid = [[10,12,4,6],[9,11,3,5],[1,7,13,8],[2,0,15,14]]
    expected = 14
    assert Solution().swimInWater(grid) == expected