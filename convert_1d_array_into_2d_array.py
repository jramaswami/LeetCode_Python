"""
LeetCode
2022. Convert 1D Array Into 2D Array
September 2024 Challenge
jramaswami
"""


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        soln = []
        if len(original) != m * n:
            return []
        g = (x for x in original)
        for r in range(m):
            row = []
            for c in range(n):
                row.append(next(g))
            soln.append(row)
        return soln
