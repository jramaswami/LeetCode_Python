"""
LeetCode
2033. Minimum Operations to Make a Uni-Value Grid
March 2025 Challenge
jramaswami
"""


from typing import List
import statistics


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # All must have same MOD(x)
        # Middle value(s) of N*X + MOD(X)
        flat = []
        for row in grid:
            for value in row:
                flat.append(value)
        rem = flat[0] % x
        if any (t % x != rem for t in flat):
            return -1
        flat = [t - rem for t in flat]
        mean = statistics.mean(flat)
        lower_bound = mean // x
        upper_bound = lower_bound + x
        return min(
            sum(abs(t - lower_bound) for t in flat) // x,
            sum(abs(t - upper_bound) for t in flat) // x
        )


def test_1():
    grid = [[2,4],[6,8]]
    x = 2
    expected = 4
    assert Solution().minOperations(grid, x) == expected


def test_2():
    grid = [[1,5],[2,3]]
    x = 1
    expected = 5
    assert Solution().minOperations(grid, x) == expected


def test_3():
    grid = [[1,2],[3,4]]
    x = 2
    expected = -1
    assert Solution().minOperations(grid, x) == expected


def test_4():
    "WA"
    grid = [[931,128],[639,712]]
    x = 73
    expected = 12
    assert Solution().minOperations(grid, x) == expected