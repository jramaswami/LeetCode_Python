"""
LeetCode :: December 2021 Challenge :: 1217. Minimum Cost to Move Chips to The Same Position
jramaswami
"""


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = sum(p % 2 for p in position)
        evens = len(position) - odds
        return min(odds, evens)
