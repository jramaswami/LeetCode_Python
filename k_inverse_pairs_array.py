"""
LeetCode :: June 2021 Challenge :: K Inverse Pairs Array
jramaswami

REF: https://dreamume.medium.com/leetcode-629-k-inverse-pairs-array-8f6b1c05e3ea
"""


class Solution:
    def kInversePairs(self, n, k):
        MOD = pow(10, 9) + 7

        if k > (n * (n - 1)) // 2 or k < 0:
            return 0

        dp = [[0 for _ in range(k+1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = 1
            if i + 1 <= n:
                dp[i + 1][0] = 1

            limit = (i * (i - 1)) // 2
            for j in range(1, min(k, limit) + 1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
                if j >= i:
                    dp[i][j] -= dp[i-1][j-i]
                dp[i][j] = (dp[i][j] + MOD) % MOD
        return dp[n][k]
