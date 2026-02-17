"""
LeetCode
401. Binary Watch
February 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        HOURS, MINUTES = 0, 1
        TIMES = (
            (1, 0), (2, 0), (4, 0), (8, 0),
            (1, 1), (2, 1), (4, 1), (8, 1), (16, 1), (32, 1)
        )

        soln = []

        def rec(i, lights_left, hours, minutes):
            if hours > 11:
                return
            if minutes > 59:
                return
            if lights_left == 0:
                soln.append(f'{hours}:{minutes:02d}')
                return
            if i >= len(TIMES):
                return

            # Skip
            rec(i+1, lights_left, hours, minutes)
            if TIMES[i][1] == HOURS:
                rec(i+1, lights_left-1, hours + TIMES[i][0], minutes)
            else:
                rec(i+1, lights_left-1, hours, minutes + TIMES[i][0])

        rec(0, turnedOn, 0, 0)
        soln.sort()
        return soln