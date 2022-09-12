"""
LeetCode :: September 2022 Challenge :: 948. Bag of Tokens
jramaswami
"""


import collections
from typing import *


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        T = collections.deque(sorted(tokens))
        max_score = 0
        curr_score = 0
        while T:
            if T[0] <= power:
                power -= T[0]
                curr_score += 1
                T.popleft()
            elif curr_score > 0:
                power += T[-1]
                curr_score -= 1
                T.pop()
            else:
                break
            max_score = max(max_score, curr_score)
        return max_score


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