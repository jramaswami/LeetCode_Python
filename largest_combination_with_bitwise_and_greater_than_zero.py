"""
LeetCode
2275. Largest Combination With Bitwise AND Greater Than Zero
November 2024 Challenge
jramaswami
"""


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        soln = 0
        for i in range(24):
            mask = (1 << i)
            soln = max(soln, sum(1 if x & mask else 0 for x in candidates))
        return soln
