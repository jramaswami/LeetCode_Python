"""
LeetCode :: December 2021 Challenge :: 1200. Minimum Absolute Difference
jramaswami
"""


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = min(b - a for a, b in zip(arr[:-1], arr[1:]))
        return [[a, b] for a, b in zip(arr[:-1], arr[1:]) if b - a == min_diff]
