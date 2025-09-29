"""
LeetCode
1039. Minimum Score Triangulation of Polygon
September 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/1039
"""


import functools


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        INF = pow(10, 10)

        @functools.cache
        def rec(left, right):
            # Base case: only two vertices left, return 0
            if left + 1 == right:
                return 0

            # Check all vertices between left and right
            min_score = INF
            for middle in range(left+1, right):
                curr_score = (
                    rec(left, middle) +
                    rec(middle, right) +
                    values[left] * values[middle] * values[right]
                )
                min_score = min(min_score, curr_score)
            return min_score

        return rec(0, len(values)-1)