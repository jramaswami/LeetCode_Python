"""
LeetCode
2943. Maximize Area of Square Hole in Grid
January 2026 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        max_width = 1
        window = collections.deque()
        for w in sorted(vBars):
            if w == 1 or w == m + 2:
                continue
            if window and window[-1] != w - 1:
                max_width = max(max_width, len(window) + 1)
                window.clear()
            window.append(w)
        max_width = max(max_width, len(window) + 1)
        max_height = 1
        window = collections.deque()
        for h in sorted(hBars):
            if h == 1 or h == n + 2:
                continue
            if window and window[-1] != h - 1:
                max_height = max(max_height, len(window) + 1)
                window.clear()
            window.append(h)

        max_height = max(max_height, len(window) + 1)
        dim = min(max_width, max_height)
        return dim * dim