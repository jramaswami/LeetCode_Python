"""
LeetCode
1140. Stone Game II
May 2023 Challenge
jramaswami
"""


import collections
import functools
from typing import *


Score = collections.namedtuple('Score', ['alice', 'bob'])


def add(score1, score2):
    return Score(score1.alice + score2.alice, score1.bob + score2.bob)


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        @functools.cache
        def rec(player, index, M):
            # Base Case
            if index >= len(piles):
                return Score(0, 0)

            result = Score(0, 0)
            if player == 'alice':
                # Choose 1 to 2*M piles
                curr_sum = 0
                for X in range(2 * M):
                    if index + X >= len(piles):
                        break
                    # Take piles[index+X]
                    curr_sum += piles[index+X]
                    # What is score if I end my turn?
                    score0 = add(Score(curr_sum, 0), rec('bob', index+X+1, max(X+1, M)))
                    if score0.alice > result.alice:
                        result = score0
            else:
                # Choose 1 to 2*M piles
                curr_sum = 0
                for X in range(2 * M):
                    if index + X >= len(piles):
                        break
                    # Take piles[index+X]
                    curr_sum += piles[index+X]
                    # What is score if I end my turn?
                    score0 = add(Score(0, curr_sum), rec('alice', index+X+1, max(X+1, M)))
                    if score0.bob > result.bob:
                        result = score0
            return result

        return rec('alice', 0, 1).alice


def test_1():
    piles = [2,7,9,4,4]
    expected = 10
    assert Solution().stoneGameII(piles) == expected


def test_2():
    piles = [1,2,3,4,5,100]
    expected = 104
    assert Solution().stoneGameII(piles) == expected