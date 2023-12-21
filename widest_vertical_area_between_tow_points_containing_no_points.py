"""
LeetCode
1637. Widest Vertical Area Between Two Points Containing No Points
December 2023 Challenge
jramaswami
"""


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        rows = list(sorted(p[0] for p in points))
        return max(b - a for a, b in zip(rows[:-1], rows[1:]))