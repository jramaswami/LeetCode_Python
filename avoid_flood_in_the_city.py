"""
LeetCode
1488. Avoid Flood in The City
October 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        soln = [-1 for _ in rains]
        sunny_days = []
        lake_filled = collections.defaultdict(lambda: -1)
        for i, lake in enumerate(rains):
            if lake == 0:
                sunny_days.append(i)
                soln[i] = 1
            else:
                # Is the lake full?
                if lake_filled[lake] >= 0:
                    # We need to empty it first. Search for
                    # the earliest day we can empty it.
                    emptied = False
                    for d, day in enumerate(sunny_days):
                        if day > lake_filled[lake]:
                            soln[day] = lake
                            sunny_days[d] *= -1
                            emptied = True
                            lake_filled[lake] = -1
                            break
                    if not emptied:
                        return []
                lake_filled[lake] = i
        return soln