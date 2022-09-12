"""
LeetCode :: September 2022 Challenge :: 948. Bag of Tokens
jramaswami
"""


import collections
from typing import *


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        T = collections.deque(sorted(tokens))
        soln = 0
        score = 0
        while T:
            while T and power < T[0]:
                power += T[-1]
                print(T[-1], "to power up")
                T.pop()
                score -= 1
            print(T, power)
            if T:
                score += 1
                power -= T[0]
                print(T[0], "for points")
                T.popleft()
            soln = max(soln, score)
        return soln


def test_1():
    tokens = [100]
    power = 50
    expected = 0
    assert Solution().bagOfTokensScore(tokens, power) == expected


def test_2():
    tokens = [100,200]
    power = 150
    expected = 1
    assert Solution().bagOfTokensScore(tokens, power) == expected


def test_3():
    tokens = [100,200,300,400]
    power = 200
    expected = 2
    assert Solution().bagOfTokensScore(tokens, power) == expected


def test_4():
    "WA"
    tokens = [71,55,82]
    power = 54
    expected =0
    assert Solution().bagOfTokensScore(tokens, power) == expected