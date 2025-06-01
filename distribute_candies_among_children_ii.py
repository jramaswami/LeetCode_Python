"""
LeetCode
2929. Distribute Candies Among Children II
June 2025 Challenge
jramaswami
"""


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Child 1 can have 0 .. min(n, limit)
        # Child 2 can have 0 .. min(n - child1, limit)
        # Child 3 must have limit - child1 - child2
        # dp[child index][candies used] = ways to reach
        dp = [[0 for _ in range(n+1)] for _ in range(3)]
        for x in range(min(n+1, limit+1)):
            dp[0][x] = 1

        for x in range(n+1):
            for t in range(limit+1):
                if x + t <= n:
                    dp[1][x+t] += dp[0][x]

        for y in range(n+1):
            for t in range(limit+1):
                if y + t <= n:
                    dp[2][y+t] += dp[1][y]

        return dp[-1][-1]


def test_1():
    n = 5
    limit = 2
    assert Solution().distributeCandies(n, limit) == 3


def test_2():
    n = 3
    limit = 3
    assert Solution().distributeCandies(n, limit) == 10

def test_3():
    n = 10001
    limit = 20001
    assert Solution().distributeCandies(n, limit) == 50025003