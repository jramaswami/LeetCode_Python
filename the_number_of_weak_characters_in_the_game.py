"""
LeetCode :: September 2022 Challenge :: 1996. The Number of Weak Characters in the Game
jramaswami
"""


import math
from typing import *


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # [attack, defense]
        # Sort properties by attack in descending order.
        properties.sort(reverse=True)
        max_defense = -math.inf
        soln = 0
        for a, d in properties:
            # Every character to my left (already seen) has an attack score higher than me.
            # Is there one that also has a defense score higher than me?
            if max_defense > d:
                # If there is then I am a weak character.
                soln += 1
            # Keep track of the highest defense score we have seen.
            max_defense = max(d, max_defense)
        return soln


def test_1():
    properties = [[5,5],[6,3],[3,6]]
    expected = 0
    assert Solution().numberOfWeakCharacters(properties) == expected


def test_2():
    properties = [[2,2],[3,3]]
    expected = 1
    assert Solution().numberOfWeakCharacters(properties) == expected


def test_3():
    properties = [[1,5],[10,4],[4,3]]
    expected = 1
    assert Solution().numberOfWeakCharacters(properties) == expected


def test_4():
    "WA"
    properties = [[1,1],[2,1],[2,2],[1,2]]
    expected = 1
    assert Solution().numberOfWeakCharacters(properties) == expected