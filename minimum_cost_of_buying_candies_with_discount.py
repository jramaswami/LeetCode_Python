"""
LeetCode
2144. Minimum Cost of Buying Candies With Discount
June 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        soln = 0
        for i, c in enumerate(cost, start=1):
            if i % 3:
                soln += c
        return soln
