"""
LeetCode
1870. Minimum Speed to Arrive on Time
July 2023 Challenge
jramaswami
"""


import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def check(speed):
            "Return if it is possible to make journey in time."
            trip_time = 0.0
            for d in dist[:-1]:
                trip_time += math.ceil(d / speed)
            trip_time += (dist[-1] / speed)
            return trip_time <= hour

        # Binary search the answer
        # lg(10^7) < 24
        # O(N lg(10^7)) = O(N * 24) = O(N)
        lo = 1
        hi = pow(10, 7)
        soln = math.inf
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                # This speed worked
                soln = min(soln, mid)
                # Try a smaller speed.
                hi = mid - 1
            else:
                # This was not fast enough.
                # Try a larger speed.
                lo = mid + 1

        return (-1 if soln == math.inf else soln)


def test_1():
    dist = [1,3,2]
    hour = 6
    expected = 1
    assert Solution().minSpeedOnTime(dist, hour) == expected


def test_2():
    dist = [1,3,2]
    hour = 2.7
    expected = 3
    assert Solution().minSpeedOnTime(dist, hour) == expected


def test_3():
    dist = [1,3,2]
    hour = 1.9
    expected = -1
    assert Solution().minSpeedOnTime(dist, hour) == expected