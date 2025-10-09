"""
LeetCode
3494. Find the Minimum Amount of Time to Brew Potions
October 2025 Challenge
jramaswami
"""


import itertools
from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        prev = list(itertools.accumulate(mana[0] * s for s in skill))
        for m in mana[1:]:
            curr = list(itertools.accumulate(m * s for s in skill))
            d = 0
            for p, c in zip(prev[1:], curr):
                d = max(d, p-c)
            curr = [c + d for c in curr]
            prev = curr
        return prev[-1]


def test_1():
    skill = [1,5,2,4]
    mana = [5,1,4,2]
    expected = 110
    assert Solution().minTime(skill, mana) == expected


def test_4():
    "WA"
    skill = [3,5,3,9]
    mana = [1,10,7,3]
    expected = 293
    assert Solution().minTime(skill, mana) == expected