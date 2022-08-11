"""
LeetCode :: 950. Reveal Cards In Increasing Order
jramaswami
"""


from typing import *
import collections


class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        deck0 = collections.deque(range(len(deck)))
        order = []
        while deck0:
            order.append(deck0.popleft())
            deck0.rotate(-1)
        soln = [0 for _ in deck]
        for i, k in zip(order, deck):
            soln[i] = k
        return soln


def test_1():
    deck = [17,13,11,2,3,5,7]
    expected = [2,13,3,11,5,17,7]
    assert Solution().deckRevealedIncreasing(deck) == expected


def test_2():
    deck = [1, 1000]
    expected = [1, 1000]
    assert Solution().deckRevealedIncreasing(deck) == expected
