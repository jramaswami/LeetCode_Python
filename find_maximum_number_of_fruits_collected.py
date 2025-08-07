"""
LeetCode
3363. Find the Maximum Number of Fruits Collected
August 2025 Challenge
jramaswami

Thank You, Larry!
REF: https://leetcode.doocs.org/en/lc/3363/#solution-1-dynamic-programming
"""


import math
from typing import List


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N = len(fruits)
        dp = [[-math.inf for _ in range(N)] for _ in range(N)]

        diagonal = 0
        for i in range(N):
            diagonal += fruits[i][i]

        # Top Right: row [1, N); column from [0, N)
        dp[0][N-1] = fruits[0][N-1]
        for row in range(1, N):
            for col in range(row + 1, N):
                for dc in (-1, 0, 1):
                    if 0 <= col + dc < N:
                        dp[row][col] = max(dp[row][col], dp[row-1][col + dc] + fruits[row][col])

        best_top_right = dp[N-2][N-1]

        # Bottom left: column [1, N); row [0, N)
        dp[N-1][0] = fruits[N-1][0]
        for col in range(1, N):
            for row in range(col + 1, N):
                for dr in (-1, 0, 1):
                    if 0 <= row + dr < N:
                        dp[row][col] = max(dp[row][col], dp[row + dr][col-1] + fruits[row][col])
        best_bottom_left = dp[N-1][N-2]

        return diagonal + best_top_right + best_bottom_left


def test_1():
    fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]
    expected = 100
    assert Solution().maxCollectedFruits(fruits) == expected


def test_2():
    fruits = [[1,1],[1,1]]
    expected = 4
    assert Solution().maxCollectedFruits(fruits) == expected


def test_3():
    "WA"
    fruits = [[16,3,11,14,14],[3,0,10,13,14],[7,18,8,7,18],[7,8,5,7,5],[0,14,8,1,0]]
    expected = 105
    assert Solution().maxCollectedFruits(fruits) == expected