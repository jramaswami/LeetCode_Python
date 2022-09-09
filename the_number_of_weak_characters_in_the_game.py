"""
LeetCode :: September 2022 Challenge :: 1996. The Number of Weak Characters in the Game
jramaswami
"""


import math
import collections
from typing import *


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # [attack, defense]
        # Sort properties by attack in descending order.
        characters_by_attack = collections.defaultdict(list)
        for a, d in properties:
            characters_by_attack[a].append(d)
        max_defense = -math.inf
        soln = 0
        for a in sorted(characters_by_attack, reverse=True):
            # Every character already seen has an attack score greater
            # than this attack score.
            # For each character with this attack score, is there a previous
            # character with higher defense score too?
            for d in characters_by_attack[a]:
                print(f"{a=} {d=} {max_defense=}")
                if max_defense > d:
                    # If there is then (a,d) is a weak character.
                    soln += 1
            # Keep track of the highest attack and defense scores we have seen.
            max_defense = max(max_defense, max(characters_by_attack[a]))
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


def test_5():
    "WA"
    properties = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
    expected = 2
    assert Solution().numberOfWeakCharacters(properties) == expected


def test_6():
    "WA"
    properties = [[10,1],[5,1],[7,10],[4,1],[5,9],[6,9],[7,2],[1,10]]
    expected = 4
    assert Solution().numberOfWeakCharacters(properties) == expected