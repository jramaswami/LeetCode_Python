"""
LeetCode :: 914. X of a Kind in a Deck of Cards
jramaswami
"""


from typing import *
import collections


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        ctr = collections.Counter(deck)
        return all(x == ctr[deck[0]] for x in ctr.values())


def test_1():
    deck = [1,2,3,4,4,3,2,1]
    expected = True
    assert Solution().hasGroupsSizeX(deck) == expected


def test_2():
    deck = [1,1,1,2,2,2,3,3]
    expected = False
    assert Solution().hasGroupsSizeX(deck) == expected


def test_3():
    "WA"
    deck = [1]
    expected = False
    assert Solution().hasGroupsSizeX(deck) == expected