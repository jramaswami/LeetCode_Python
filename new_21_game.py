"""
LeetCode
837. New 21 Game
May 2023 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=zKi4LzjK27k
"""


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or k + maxPts <= n:
            return 1.0

        windowSum = 0
        for i in range(k, k+ maxPts):
            windowSum += 1 if i <= n else 0

        dp = {}
        for i in range(k - 1, -1, -1):
            dp[i] = windowSum / maxPts

            remove = 0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts, 1)
            windowSum += dp[i] - remove

        return dp[0]


EPS = pow(10, -5)


def test_1():
    n = 10
    k = 1
    maxPts = 10
    expected = 1.00000
    assert abs(Solution().new21Game(n, k, maxPts) - expected) < EPS


def test_2():
    n = 6
    k = 1
    maxPts = 10
    expected = 0.60000
    assert abs(Solution().new21Game(n, k, maxPts) - expected) < EPS


def test_3():
    n = 21
    k = 17
    maxPts = 10
    expected = 0.73278
    assert abs(Solution().new21Game(n, k, maxPts) - expected) < EPS
