"""
LeetCode :: January 2022 Challenge :: 849. Maximize Distance to Closest Person
jramaswami
"""


import math


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        left = [math.inf for _ in seats]
        right = [math.inf for _ in seats]

        for i, n in enumerate(seats):
            if n:
                left[i] = 0
            else:
                left[i] = left[i-1] + 1 if i > 0 else math.inf

        for off, n in enumerate(reversed(seats)):
            i = len(seats) - off - 1
            if n:
                right[i] = 0
            else:
                right[i] = right[i+1] + 1 if i + 1 < len(seats) else math.inf

        soln = 0
        for l, r in zip(left, right):
            d = min(l, r)
            soln = max(soln, d)
        return soln
