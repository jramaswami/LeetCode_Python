"""
LeetCode :: October 2021 Challenge :: 279. Perfect Squares
jramaswami
"""


class Solution:

    def __init__(self):
        # Cache the squares up to the maximum n.
        max_n = pow(10, 4)
        self.squares = []
        for k in range(1, max_n):
            sq = k * k
            if sq > max_n:
                break
            self.squares.append(sq)


    def numSquares(self, n):
        useful_squares = [k for k in self.squares if k <= n]
        # At worst, you can reach n by adding n ones.
        dp = [n for _ in range(n+1)]

        # However, we can reach each perfect square in just 1.
        for k in useful_squares:
            dp[k] = 1

        # Dynamic programming to update every possible value j + k where
        # k is a perfect square.
        for j, _ in enumerate(dp):
            for k in useful_squares:
                if j + k > n:
                    break
                dp[j + k] = min(dp[j + k], dp[j] + 1)

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
