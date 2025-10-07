"""
LeetCode
1488. Avoid Flood in The City
October 2025 Challenge
jramaswami
"""


import sortedcontainers
from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        soln = [-1 for _ in rains]
        sunny_days = sortedcontainers.SortedList()
        lake_filled = dict()
        for i, lake in enumerate(rains):
            if lake == 0:
                sunny_days.add(i)
                soln[i] = 1
            else:
                # Is the lake full?
                if lake in lake_filled:
                    # We need to empty it first. Search for
                    # the earliest day we can empty it. That
                    # day must be *after* the day it was
                    # previously filled.
                    d = sunny_days.bisect_right(lake_filled[lake])
                    if d == len(sunny_days):
                        return []
                    soln[sunny_days[d]] = lake
                    # We used the sunny day, remove it.
                    sunny_days.pop(d)
                lake_filled[lake] = i
        return soln