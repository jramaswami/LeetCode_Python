"""
LeetCode
1840. Maximum Building Height
June 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        limit = list(range(n))
        for i, k in restrictions:
            limit[i-1] = k
        for i, curr in enumerate(limit[1:], start=1):
            prev = limit[i-1]
            limit[i] = min(curr, prev+1)
        for i in range(n-2, -1, -1):
            prev = limit[i+1]
            curr = limit[i]
            limit[i] = min(curr, prev+1)
        return max(limit)