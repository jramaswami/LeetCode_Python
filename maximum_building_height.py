"""
LeetCode
1840. Maximum Building Height
June 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        INDEX, LIMIT = 0, 1
        restrictions.append([1, 0])
        restrictions.sort()
        if restrictions[-1][INDEX] != n:
            restrictions.append([n, n])

        for i in range(1, len(restrictions)):
            x, prev = restrictions[i-1]
            y, curr = restrictions[i]
            delta = y - x
            restrictions[i][LIMIT] = min(prev + delta, curr)

        for i in range(len(restrictions)-2, -1, -1):
            x, prev = restrictions[i+1]
            y, curr = restrictions[i]
            delta = x - y
            restrictions[i][LIMIT] = min(prev + delta, curr)

        soln = 0
        for i, _ in enumerate(restrictions[:-1]):
            x, prev = restrictions[i]
            y, curr = restrictions[i+1]
            dist = y - x
            delta = abs(curr - prev)
            k = max(prev, curr) + ((dist - delta) // 2)
            soln = max(soln, k)
        return soln