"""
LeetCode
3633. Earliest Finish Time for Land and Water Rides I
June 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        soln = pow(10, 10)
        for land_start, land_dur in zip(landStartTime, landDuration):
            for water_start, water_dur in zip(waterStartTime, waterDuration):
                # Land first
                le = land_start + land_dur
                ws = max(le, water_start)
                we = ws + water_dur
                soln = min(soln, we)
                # Water first
                we = water_start + water_dur
                ls = max(we, land_start)
                le = ls + land_dur
                soln = min(soln, le)
        return soln
