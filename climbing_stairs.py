"""
LeetCode :: October 2021 Challenge :: 70. Climbing Stairs
jramaswami
"""


class Solution:

    def climbStairs(self, steps):
        dp = [0 for _ in range(steps+1)]
        dp[0] = 1
        for i, k in enumerate(dp):
            if i + 1 < len(dp):
                dp[i+1] += k
            if i + 2 < len(dp):
                dp[i+2] += k
        return dp[-1]


def test_1():
    assert Solution().climbStairs(2) == 2


def test_2():
    assert Solution().climbStairs(3) == 3


def test_3():
    assert Solution().climbStairs(45) == 1836311903
