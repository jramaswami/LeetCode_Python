"""
Leet Code :: May 2022 Challenge :: Unique Paths II
jramaswami
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        dp = [[0 for _ in row] for row in obstacleGrid]

        def get(r, c):
            if r < 0 or c < 0:
                return 0
            return dp[r][c]

        for r, row in enumerate(obstacleGrid):
            for c, val in enumerate(row):
                if val == 0:
                    if r == 0 and c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = get(r - 1, c) + get(r, c - 1)

        return dp[-1][-1]


def test_1():
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    assert Solution().uniquePathsWithObstacles(obstacleGrid) == 2


def test_2():
    obstacleGrid = [[0,1],[0,0]]
    assert Solution().uniquePathsWithObstacles(obstacleGrid) == 1


def test_3():
    obstacleGrid = [[1]]
    assert Solution().uniquePathsWithObstacles(obstacleGrid) == 0
