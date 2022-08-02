"""
LeetCode :: August 2022 Challenge :: 62. Unique Paths
jramaswami
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for r, row in enumerate(dp):
            for c, _ in enumerate(row):
                if c + 1 < n:
                    dp[r][c+1] += dp[r][c]
                if r + 1 < m:
                    dp[r+1][c] += dp[r][c]
        return dp[-1][-1]


def test_1():
    m = 3
    n = 7
    expected = 28
    assert Solution().uniquePaths(m, n) == expected


def test_2():
    m = 3
    n = 2
    expected = 3
    assert Solution().uniquePaths(m, n) == expected