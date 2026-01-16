"""
LeetCode
2975. Maximum Square Area by Removing Fences From a Field
January 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences0 = [1]
        hFences0.extend(sorted(hFences))
        hFences0.append(m)
        vFences0 = [1]
        vFences0.extend(sorted(vFences))
        vFences0.append(n)
        hDeltas = set()
        for i, a in enumerate(hFences0):
            for b in hFences0[i+1:]:
                delta = b - a
                hDeltas.add(delta)
        vDeltas = set()
        for i, a in enumerate(vFences0):
            for b in vFences0[i+1:]:
                delta = b - a
                vDeltas.add(delta)
        MOD = pow(10, 9) + 7
        dim = 0
        for h in hDeltas:
            if h in vDeltas:
                dim = max(dim, h)
        return (dim * dim) % MOD if dim else -1