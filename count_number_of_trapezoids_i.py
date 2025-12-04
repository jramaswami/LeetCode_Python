"""
LeetCode
3623. Count Number of Trapezoids I
December 2025 Challenge
jramaswami
"""


import collections
import math


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        points_by_y = collections.defaultdict(int)
        for x, y in points:
            points_by_y[y] += 1

        MOD = pow(10, 9) + 7
        nc2 = [math.comb(n, 2) % MOD for n in points_by_y.values()]
        total = 0
        for x in nc2:
            total += x
            total %= MOD

        soln = 0
        for x in nc2:
            total = total - x + MOD
            total %= MOD
            t = x * total
            t %= MOD
            soln += t
            soln %= MOD
        return soln % MOD