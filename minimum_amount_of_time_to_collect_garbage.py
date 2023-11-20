"""
LeetCode
2391. Minimum Amount of Time to Collect Garbage
November 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        pickup_count = {t: 0 for t in 'GPM'}
        travel_max = {t: 0 for t in 'GPM'}
        curr_travel = 0
        for i, house in enumerate(garbage):
            # Pickup any garbage at this huse
            for t in house:
                pickup_count[t] += 1
                travel_max[t] = max(travel_max[t], curr_travel)
            # Travel to next house
            if i < len(travel):
                curr_travel += travel[i]
        return sum(pickup_count.values()) + sum(travel_max.values())