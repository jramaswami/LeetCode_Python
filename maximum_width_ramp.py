"""
LeetCode :: 962. Maximum Width Ramp
jramaswami
"""


from typing import *


class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:
        nums0 = [(n, i) for i, n in enumerate(nums)]
        nums0.sort(reverse=True)
        curr_max = -1
        soln = 0
        prev = None
        for n, i in nums0:
            soln = max(soln, curr_max - i)
            curr_max = max(curr_max, i)
        return soln


def test_1():
    nums = [6,0,8,2,1,5]
    expected = 4
    assert Solution().maxWidthRamp(nums) == expected


def test_2():
    nums = [9,8,1,0,1,9,4,0,4,1]
    expected = 7
    assert Solution().maxWidthRamp(nums) == expected
