"""
LeetCode
2145. Count the Hidden Sequences
April 2025 Challenge
jramaswami
"""


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        INF = pow(10, 10)
        min_delta = INF
        max_delta = -INF
        curr_delta = 0
        for d in differences:
            curr_delta += d
            min_delta = min(min_delta, curr_delta)
            max_delta = max(max_delta, curr_delta)
        lower_bound = max(lower - min_delta, lower)
        upper_bound = min(upper - max_delta, upper)
        if lower_bound <= upper_bound:
            return upper_bound - lower_bound + 1
        return 0