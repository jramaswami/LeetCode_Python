"""
LeetCode
1503. Last Moment Before All Ants Fall Out of a Plank
November 2023 Challenge
jramaswami

Key insight: the ants striking each other and turning is equivalent to the
ants just continuing in the same direction.
"""


import math
from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        soln = -math.inf
        for i in left:
            # Going towards zero, so distance = i
            soln = max(soln, i)
        for i in right:
            # Goin towards n so distance is n - i
            soln = max(soln, n - i)
        return soln