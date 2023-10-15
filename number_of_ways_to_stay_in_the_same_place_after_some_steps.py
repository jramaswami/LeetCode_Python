"""
LeetCode
1269. Number of Ways to Stay in the Same Place After Some Steps
October 2023 Challenge
jramaswami
"""


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = pow(10, 9) + 7
        # dp[step][index] = number of ways to reach position (index) on this step
        # index is limited to a maximum of steps because that is the farthest
        # index that can be reached on the last step
        dp = [[0 for _ in range(min(steps+1, arrLen))] for _ in range(steps+1)]
        dp[0][0] = 1   # Start at position 0
        for s, step_row in enumerate(dp[:-1]):
            for i, x in enumerate(step_row):
                if i - 1 >= 0:
                    dp[s+1][i-1] += x
                    dp[s+1][i-1] %= MOD
                dp[s+1][i] += x
                dp[s+1][i] %= MOD
                if i + 1 < len(dp[s+1]):
                    dp[s+1][i+1] += x
                    dp[s+1][i+1] %= MOD
        return dp[-1][0]


def test_1():
    steps = 3
    arrLen = 2
    expected = 4
    assert Solution().numWays(steps, arrLen) == expected


def test_2():
    steps = 2
    arrLen = 4
    expected = 2
    assert Solution().numWays(steps, arrLen) == expected


def test_3():
    steps = 4
    arrLen = 2
    expected = 8
    assert Solution().numWays(steps, arrLen) == expected


def test_4():
    steps = 430
    arrLen = 148488
    expected = 525833932
    assert Solution().numWays(steps, arrLen) == expected