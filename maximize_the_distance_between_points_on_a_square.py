"""
LeetCode
3464. Maximize the Distance Between Points on a Square
April 2026 Challenge
jramaswami
REF: https://www.youtube.com/watch?v=0Y3AIaK0Qp4
"""


import bisect
from typing import List


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        n = len(points)
        distance = [] # distance from 0,0
        for x, y in points:
            if y == 0: distance.append(x)
            elif y == side: distance.append(side * 2 + (side - x))
            elif x == 0: distance.append(side * 3 + (side - y))
            elif x == side: distance.append(side + y)
        distance.sort()

        def check(mn):
            for i in range(n):
                count = 1
                curr = i
                while count < k:
                    jump = bisect.bisect_left(distance, distance[curr] + mn)
                    if jump == len(distance):
                        return False
                    if distance[i] + 4 * side - distance[jump] < mn: break
                    count += 1
                    curr = jump
                if count == k:
                    return True
            return False

        low = 1
        high = 2 * side
        while low < high:
            mid = low + ((high - low + 1) // 2)
            if check(mid):
                low = mid
            else:
                high = mid - 1
        return low