"""
LeetCode
1289. Minimum Falling Path Sum II
April 2024 Challenge
jramaswami
"""


from typing import List
import heapq
import collections


RowMin = collections.namedtuple('RowMin', ['value', 'index'])


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        row_mins = []
        for row in grid:
            row_mins.append(heapq.nsmallest(2, (RowMin(x, i) for i, x in enumerate(row))))

        dp = [[None for _ in row] for row in row_mins]
        dp [0] = [t[0] for t in row_mins[0]]
        for r, _ in enumerate(row_mins[1:], start=1):
            if row_mins[r][0].index == row_mins[r-1][0].index:
                dp[r][0] = row_mins[r][0].value + dp[r-1][1]
            else:
                dp[r][0] = row_mins[r][0].value + dp[r-1][0]

            if row_mins[r][1].index == row_mins[r-1][1].index:
                dp[r][1] = row_mins[r][1].value + dp[r-1][0]
            else:
                dp[r][1] = row_mins[r][1].value + dp[r-1][1]

        return min(dp[-1])


def test_1():
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    expected = 13
    result = Solution().minFallingPathSum(grid)
    assert result == expected


def test_2():
    grid = [[7]]
    expected = 7
    result = Solution().minFallingPathSum(grid)
    assert result == expected


def test_3():
    "WA"
    grid = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]
    expected = -192
    result = Solution().minFallingPathSum(grid)
    assert result == expected