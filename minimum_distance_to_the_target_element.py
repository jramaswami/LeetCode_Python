"""
LeetCode
1848. Minimum Distance to the Target Element
April 2026 Challenge
jramaswami
"""


import math
from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        soln = math.inf
        for i, x in enumerate(nums):
            if x == target:
                soln = min(soln, abs(i-start))
        return soln