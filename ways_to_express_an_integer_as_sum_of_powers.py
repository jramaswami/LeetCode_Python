"""
LeetCode
2787. Ways to Express an Integer as Sum of Powers
August 2025 Challenge
jramaswami
"""


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = pow(10,9)+7
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        dp [0][0] = 1
        for i in range(1, n+1):
            t = pow(i, x)
            for j in range(n+1):
                dp[i][j] += dp[i-1][j]
                dp[i][j] %= MOD
                if j + t < n+1:
                    dp[i][j+t] += dp[i-1][j]
                    dp[i][j+t] %= MOD

        return dp[-1][-1] % MOD