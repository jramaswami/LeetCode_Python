"""
LeetCode :: March 2021 Challenge :: Wiggle Subsequence
jramaswami
"""
from typing import *
from math import inf


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def wiggle0(index, last_num, increasing, length):
            if index >= len(nums):
                return length

            soln = -inf
            # If this in an increasing start and nums[index] is greater than
            # the last number then we can add nums[index] to the sequence.
            if increasing and nums[index] > last_num:
                soln = max(soln, wiggle0(index + 1, nums[index], False, length + 1))
            # Same for decreasing
            if not increasing and nums[index] < last_num:
                soln = max(soln, wiggle0(index + 1, nums[index], True, length + 1))
            # We can also just skip nums[index]
            soln = max(soln, wiggle0(index + 1, last_num, increasing, length))

            return soln

        return max(wiggle0(0, -inf, True, 0), wiggle0(0, inf, False, 0))


def test_1():
    nums = [1,7,4,9,2,5]
    assert Solution().wiggleMaxLength(nums) == 6

def test_2():
    nums = [1,2,3,4,5,6,7,8,9]
    assert Solution().wiggleMaxLength(nums) == 2

def test_3():
    """TLE"""
    nums = [33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]
    assert Solution().wiggleMaxLength(nums) == 0
