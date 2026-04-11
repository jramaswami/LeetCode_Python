"""
LeetCode
3741. Minimum Distance Between Three Equal Elements II
April 2026 Challenge
jramaswami
"""


import collections
import math
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        values = collections.defaultdict(list)
        for i, n in enumerate(nums):
            values[n].append(i)
        soln = math.inf
        for n in values:
            if len(values[n]) >= 3:
                p = 0
                while p + 2 < len(values[n]):
                    i = values[n][p]
                    k = values[n][p+2]
                    soln = min(soln, 2*k - 2*i)
                    p += 1
        return soln if soln < math.inf else -1