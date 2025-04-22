"""
LeetCode
2338. Count the Number of Ideal Arrays
April 2025 Challenge
jramawami
"""



class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = pow(10, 9) + 7
        # dp[i][j] = number of ways where 0 <= i < n and 0 <= j <= maxValue
        dp = [[0 for _ in range(maxValue+1)] for _ in range(n)]
        # Initialize initial row
        dp[0] = [1 for _ in range(maxValue+1)]
        for i in range(n-1):
            for j in range(1, maxValue+1):
                for k in range(j, maxValue+1, j):
                    dp[i+1][k] += dp[i][j]
                    dp[i+1][k] %= MOD

        for row in dp:
            print(row)
        soln = 0
        for t in dp[-1]:
            soln += t
            soln %= MOD
        return soln % MOD


def test_1():
    n = 2
    maxValue = 5
    expected = 10
    assert Solution().idealArrays(n, maxValue) == expected


def test_2():
    n = 5
    maxValue = 3
    expected = 11
    assert Solution().idealArrays(n, maxValue) == expected
