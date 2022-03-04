"""
LeetCode :: March 2022 Challenge :: 799. Champagne Tower
jramaswami
"""


class Solution:

    def champagneTower(self, poured, query_row, query_glass):
        limits = [1]
        while len(limits) < 100:
            limits.append(limits[-1] * 2)

        dp = [[0 for _ in range(100)] for _ in range(100)]
        dp[0][0] = poured
        for r, row in enumerate(dp[:-1]):
            for c, _ in enumerate(row):
                if dp[r][c] > limits[r]:
                    dp[r+1][c] += dp[r][c] - limits[r]
                    dp[r+1][c+1] += dp[r][c] - limits[r]
                    dp[r][c] = limits[r]

        return dp[query_row][query_glass] / limits[query_row]


def test_1():
    poured = 1
    query_row = 1
    query_glass = 1
    expected = 0.00000
    assert Solution().champagneTower(poured, query_row, query_glass) == expected


def test_2():
    poured = 2
    query_row = 1
    query_glass = 1
    expected = 0.50000
    assert Solution().champagneTower(poured, query_row, query_glass) == expected


def test_3():
    poured = 100000009
    query_row = 33
    query_glass = 17
    expected = 1.00000
    assert Solution().champagneTower(poured, query_row, query_glass) == expected


def test_4():
    "WA"
    poured = 25
    query_row =  6
    query_glass = 1
    expected = 0.18750
    assert Solution().champagneTower(poured, query_row, query_glass) == expected
