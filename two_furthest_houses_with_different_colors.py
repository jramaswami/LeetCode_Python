"""
LeetCode
2078. Two Furthest Houses With Different Colors
April 2026 Challenge
jramaswami
"""


import collections
import math
from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        min_locs = collections.defaultdict(lambda: math.inf)
        max_locs = collections.defaultdict(lambda: -math.inf)
        for i, color in enumerate(colors):
            min_locs[color] = min(min_locs[color], i)
            max_locs[color] = max(max_locs[color], i)

        soln = -math.inf
        for curr_color in min_locs:
            min_curr, max_curr = min_locs[curr_color], max_locs[curr_color]
            for other_color in min_locs:
                if curr_color != other_color:
                    min_other, max_other = min_locs[other_color], max_locs[other_color]
                    for a in (min_curr, max_curr):
                        for b in (min_other, max_other):
                            soln = max(soln, abs(a - b))
        return soln