"""
LeetCode
403. Frog Jump
August 2023 Challenge
jramaswami
"""


import bisect
import functools
from typing import *



class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # invariant: stones is sorted

        def index(a, x):
            'Locate the leftmost value exactly equal to x'
            i = bisect.bisect_left(a, x)
            if i != len(a) and a[i] == x:
                return i
            return -1

        @functools.cache
        def rec(curr_stone_index, prev_jump):
            if curr_stone_index == len(stones) - 1:
                return True

            possible_jumps = [prev_jump+o for o in (-1, 0, 1) if prev_jump+o > 0]
            for jump in possible_jumps:
                jump_to_stone = stones[curr_stone_index] + jump
                jump_to_index = index(stones, jump_to_stone)

                if jump_to_index > -1:
                    if rec(jump_to_index, jump):
                        return True
            return False

        return rec(0, 0)


def test_1():
    stones = [0,1,3,5,6,8,12,17]
    expected = True
    assert Solution().canCross(stones) == expected


def test_2():
    stones = [0,1,2,3,4,8,9,11]
    expected = False
    assert Solution().canCross(stones) == expected