"""
LeetCode
1878. Get Biggest Three Rhombus Sums in a Grid
March 2026 Challenge
jramaswami

Thank You Larry!
"""


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])
        values = SortedSet()

        def get_sum(x, y, L):
            if L == 0:
                return grid[x][y]
            total = 0
            cx, cy = x - L, y
            for dx, dy in ((1, 1), (1, -1), (-1, -1), (-1, 1)):
                for _ in range(L):
                    cx += dx
                    cy += dy
                    total += grid[cx][cy]
            return total

        for x in range(R):
            for y in range(C):
                L = 0
                while x - L >= 0 and x + L < R and y - L >= 0 and y + L < C:
                    t = get_sum(x, y, L)
                    values.add(t)
                    if len(values) > 3:
                        values.remove(values[0])
                    L += 1
        return list(reversed(values))