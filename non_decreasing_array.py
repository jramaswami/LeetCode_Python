"""
Leet Code :: May 2021 Challenge :: Non-decreasing Array
jramaswami
"""
from typing import *


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nondecr = 0
        for a, b in zip(nums[:-1], nums[1:]):
            if a > b:
                nondecr += 1
        return nondecr <= 1


def test_1():
    nums = [4,2,3]
    assert Solution().checkPossibility(nums) == True


def test_2():
    nums = [4,2,1]
    assert Solution().checkPossibility(nums) == False


def test_3():
    """WA"""
    nums = [3,4,2,3]
    assert Solution().checkPossibility(nums) == False