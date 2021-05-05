"""
Leet Code :: Jump Game II
jramaswami
"""
from typing import *
from collections import namedtuple


Ladder = namedtuple('Ladder', ['start', 'end'])


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        current_ladder = Ladder(0, nums[0])
        waiting_ladder = Ladder(0, -1)
        ladders_used = 1
        finished = len(nums) - 1
        for i, n in enumerate(nums[1:], start=1):
            if current_ladder.end < i:
                current_ladder = waiting_ladder
                ladders_used += 1
            ladder = Ladder(i, i + n)
            if ladder.end > waiting_ladder.end:
                waiting_ladder = ladder
        return ladders_used


def test_1():
    nums = [2,3,1,1,4]
    assert Solution().jump(nums) == 2


def test_2():
    nums = [2,3,0,1,4]
    assert Solution().jump(nums) == 2


def test_3():
    nums = [2,3,1,1,4,2,3,1,1,4,2,3,1,1,4]
    assert Solution().jump(nums) == 6


def test_4():
    nums = [2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4,2,3,1,1,4]
    assert Solution().jump(nums) == 42


def test_5():
    nums = [0]
    assert Solution().jump(nums) == 0
