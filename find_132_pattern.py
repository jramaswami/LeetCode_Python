"""
LeetCode :: May 2022 Challenge :: 456. 132 Pattern
jramaswami
"""


import math


class Solution:

    def find132pattern(self, nums):
        curr_min = math.inf
        for i, n in enumerate(nums):
            if n > curr_min:
                if any(curr_min < m < n for m in nums[i+1:]):
                    return True
            curr_min = min(curr_min, n)
        return False


def test_1():
    nums = [1,2,3,4]
    expected = False
    assert Solution().find132pattern(nums) == expected


def test_2():
    nums = nums = [3,1,4,2]
    expected = True
    assert Solution().find132pattern(nums) == expected


def test_3():
    "WA"
    nums = [1,0,1,-4,-3]
    expected = False
    assert Solution().find132pattern(nums) == expected


def test_4():
    "WA"
    nums = [3,5,0,3,4]
    expected = True
    assert Solution().find132pattern(nums) == expected