"""
LeetCode
1503. Last Moment Before All Ants Fall Out of a Plank
November 2023 Challenge
jramaswami
"""


from typing import List
import itertools


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(itertools.chain(left, right))