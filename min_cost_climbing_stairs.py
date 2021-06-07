"""
LeetCode :: June 2021 Challenge :: Min Cost Climbing Stairs
jramaswami
"""


from typing import *
from math import inf


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [inf for _ in cost]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i, v in enumerate(dp):
            if i + 1 < len(dp):
                dp[i + 1] = min(dp[i + 1], dp[i] + cost[i + 1])
            if i + 2 < len(dp):
                dp[i + 2] = min(dp[i + 2], dp[i] + cost[i + 2])
        return min(dp[-2], dp[-1])


def test_1():
    cost = [10,15,20]
    expected = 15
    assert Solution().minCostClimbingStairs(cost) == expected


def test_2():
    cost = [1,100,1,1,1,100,1,1,100,1]
    expected = 6
    assert Solution().minCostClimbingStairs(cost) == expected
