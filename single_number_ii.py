"""
LeetCode :: Single Number II
jramaswami
"""
from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        soln = 0
        for bit in range(33):
            mask = 1 << bit
            set_count = 0
            for n in nums:
                if mask & n:
                    set_count += 1
            if set_count % 3:
                soln |= mask
        return soln
        

def test_1():
    """WA"""
    nums = [-2,-2,1,1,4,1,4,4,-4,-2]
    assert Solution().singleNumber(nums) == -4



