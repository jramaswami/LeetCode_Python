"""
LeetCode :: 485. Max Consecutive Ones
jramaswami
"""
from typing import *

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        run_length = 0
        max_run_length = 0
        for value in nums:
            if value == 1:
                run_length += 1
            else:
                max_run_length = max(max_run_length, run_length)
                run_length = 0
        max_run_length = max(max_run_length, run_length)
        return max_run_length


def test_1():
    assert Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3

def test_2():
    assert Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]) == 2
