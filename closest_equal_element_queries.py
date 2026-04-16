"""
LeetCode
3488. Closest Equal Element Queries
April 2026 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        locations = collections.defaultdict(list)
        for i, x in enumerate(nums):
            locations[x].append(i)
        N = len(nums)
        nearest = [-1 for _ in nums]
        for x in locations:
            n = len(locations[x])
            if n > 1:
                for i, y in enumerate(locations[x]):
                    left_neighbor = locations[x][(i - 1 + n) % n]
                    right_neighbor = locations[x][(i + 1) % n]
                    nearest[y] = min(
                        (N + y - left_neighbor) % N,
                        (N + left_neighbor - y) % N,
                        (N + y - right_neighbor) % N,
                        (N + right_neighbor - y) % N,
                    )
        return [nearest[i] for i in queries]