"""
Leet Code :: June 2022 Challenge :: Running Sum of 1d Array
jramaswami
"""


import itertools


class Solution:
    def runningSum(self, nums):
        return list(itertools.accumulate(nums))


def test_1():
    nums = [1,2,3,4]
    expected = [1,3,6,10]
    assert Solution().runningSum(nums) == expected


def test_2():
    nums = [1,1,1,1,1]
    expected = [1,2,3,4,5]
    assert Solution().runningSum(nums) == expected


def test_3():
    nums = [3,1,2,10,1]
    expected = [3,4,6,16,17]
    assert Solution().runningSum(nums) == expected
