"""
LeetCode
2270. Number of Ways to Split Array
January 2025 Challenge
jramaswami
"""


import itertools
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        soln = 0
        prefix_sums = list(itertools.accumulate(nums))
        suffix_sum = 0
        for i in range(len(nums) - 1, 0, -1):
            # Splitting array nums[:i], nums[i:]
            suffix_sum += nums[i]
            if prefix_sums[i-1]  >= suffix_sum:
                soln += 1
        return soln


def test1():
    nums = [10,4,-8,7]
    expected = 2
    assert Solution().waysToSplitArray(nums) == expected
        

def test2():
    nums = [2,3,1,0]
    expected = 2
    assert Solution().waysToSplitArray(nums) == expected
