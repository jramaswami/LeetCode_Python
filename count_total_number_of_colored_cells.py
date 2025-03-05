"""
LeetCode
2579. Count Total Number of Colored Cells
March 2025 Challenge
jramaswami
"""


class Solution:
    def coloredCells(self, n: int) -> int:
        # OEIS A001844
        n -= 1
        return n**2 + (n+1)**2
