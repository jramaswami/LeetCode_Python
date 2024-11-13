"""
LeetCode
2563. Count the Number of Fair Pairs
November 2024 Challenge
jramaswami
"""


import sortedcontainers


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        soln = 0
        seen = sortedcontainers.SortedList()
        for x in nums:
            # lower <= x + y --> lower - x >= y
            y = lower - x
            i = seen.bisect_left(y)
            # x + y <= upper  --> y <= upper - x
            y = upper - x
            j = seen.bisect_right(y)
            soln += (j - i)
            seen.add(x)
        return soln
