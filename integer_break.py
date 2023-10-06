"""
LeetCode
343. Integer Break
October 2023 Challenge
jramaswami
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = dp[2] = 1
        for i in range(3, n+1):
            for a in range(1, i):
                dp[i] = max(dp[i], a * (i-a))
                dp[i] = max(dp[i], a * dp[i-a])
        return dp[n]



def test_1():
    assert Solution().integerBreak(2) == 1


def test_2():
    assert Solution().integerBreak(10) == 36