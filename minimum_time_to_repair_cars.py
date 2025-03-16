"""
LeetCode
2594. Minimum Time to Repair Cars
March 2025 Challenge
jramaswami
"""


import math
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def cars_repaired(m, r):
            """
            where m = minutes, r = mechanic's rank, n = number of cars
            m = r * n * n
            m / r = n * n
            sqrt(m / r) = n
            """
            return int(math.sqrt(m / r))

        def check(m):
            t = [cars_repaired(m, r) for r in ranks]
            return sum(t) >= cars

        low = 0
        high = pow(10, 8)
        soln = high
        while low <= high:
            mid = low + ((high - low) // 2)
            if check(mid):
                soln = min(soln, mid)
                high = mid - 1
            else:
                low = mid + 1
        return soln


def test_1():
    ranks = [4,2,3,1]
    cars = 10
    expected = 16
    assert Solution().repairCars(ranks, cars) == expected