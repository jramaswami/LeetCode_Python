"""
LeetCode
2706. Buy Two Chocolates
December 2023 Challenge
jramaswami
"""


import heapq


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        t = money - sum(heapq.nsmallest(2, prices))
        if t >= 0:
            return t
        return money