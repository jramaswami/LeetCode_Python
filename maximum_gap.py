"""
LeetCode :: May 2021 Challenge :: Maximum Gap
jramaswami
"""


from typing import *


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        nums0 = sorted(nums)
        return max(b - a for a, b in zip(nums0, nums0[1:]))


def test_1():
    nums = [3,6,9,1]
    assert Solution().maximumGap(nums) == 3


def test_2():
    nums = [10]
    assert Solution().maximumGap(nums) == 0