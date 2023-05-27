"""
LeetCode
1406. Stone Game III
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
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @functools.cache
        def rec(player, index):
            # Base Case
            if index >= len(stoneValue):
                return Score(0, 0)

            if player == 'Alice':
                best_alice = Score(0, 0)
                curr_score = 0
                for offset in range(0, 3):
                    if index + offset >= len(stoneValue):
                        break
                    # Take stone
                    curr_score += stoneValue[index + offset]
                    # What would the score be if I ended my turn?
                    result = add(Score(curr_score, 0), rec('Bob', index + offset + 1))
                    if (result.alice > best_alice.alice):
                        best_alice = result
                return best_alice
            else:
                best_bob = Score(0, 0)
                curr_score = 0
                for offset in range(0, 3):
                    if index + offset >= len(stoneValue):
                        break
                    # Take stone
                    curr_score += stoneValue[index + offset]
                    # What would the score be if I ended my turn?
                    result = add(Score(0, curr_score), rec('Alice', index + offset + 1))
                    if (result.bob > best_bob.bob):
                        best_bob = result
                return best_bob

        soln = rec('Alice', 0)
        if soln.alice > soln.bob:
            return 'Alice'
        elif soln.bob > soln.alice:
            return 'Bob'
        return 'Tie'


def test_1():
    values = [1,2,3,7]
    expected = 'Bob'
    assert Solution().stoneGameIII(values) == expected


def test_2():
    values = [1,2,3,-9]
    expected = 'Alice'
    assert Solution().stoneGameIII(values) == expected


def test_3():
    values = [1,2,3,6]
    expected = 'Tie'
    assert Solution().stoneGameIII(values) == expected


def test_4():
    "WA"
    values = [-2]
    expected = 'Bob'
    assert Solution().stoneGameIII(values) == expected