"""
LeetCode :: October 2021 Challenge :: 279. Perfect Squares
jramaswami
"""


class Solution:
    def numSquares(self, n):
        # At worst, you can reach n by adding n ones.
        dp = [n for _ in range(n+1)]

        # However, we can reach each perfect square in just 1.
        for k in range(n):
            sq = k * k
            if sq > n:
                break
            dp[sq] = 1

        # Dynamic programming to update every possible value j + k where
        # k is a perfect square.
        for j, _ in enumerate(dp):
            for k in range(n):
                sq = k * k
                if j + sq > n:
                    break
                dp[j + sq] = min(dp[j + sq], dp[j] + 1)

        return dp[-1]


def test_1():
    assert Solution().numSquares(12) == 3


def test_2():
    assert Solution().numSquares(13) == 2


def test_3():
    """TLE"""
    assert Solution().numSquares(351) == 4


def test_4():
    """TLE"""
    assert Solution().numSquares(4586) == 2
