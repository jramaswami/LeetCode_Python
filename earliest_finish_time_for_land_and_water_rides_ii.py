"""
LeetCode
3635. Earliest Finish Time for Land and Water Rides II
June 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_land_finish = min(s + d for s, d in zip(landStartTime, landDuration))
        land_soln = min(max(start, min_land_finish) + dur for start, dur in zip(waterStartTime, waterDuration))
        min_water_finish = min(s + d for s, d in zip(waterStartTime, waterDuration))
        water_soln = min(max(start, min_water_finish) + dur for start, dur in zip(landStartTime, landDuration))
        return min(land_soln, water_soln)
