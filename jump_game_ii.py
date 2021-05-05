"""
Leet Code :: Jump Game II
jramaswami
"""
from typing import *


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        jumps_made = 1
        left = 0
        right = nums[0]
        finish = len(nums) - 1
        while right < finish:
            jumps_made += 1
            left, right = right, max(i + n for i, n in enumerate(nums[left:right+1], start=left))
        return jumps_made


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
