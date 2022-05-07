"""
LeetCode :: May 2022 Challenge :: 456. 132 Pattern
jramaswami
"""


import itertools


class Solution:

    def find132pattern(self, nums):
        min_left = list(itertools.accumulate(nums, min))
        min_right = list(reversed(list(itertools.accumulate(reversed(nums), min))))
        for n, ml, mr in zip(nums, min_left, min_right):
            if n != ml and n != mr:
                return True
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
