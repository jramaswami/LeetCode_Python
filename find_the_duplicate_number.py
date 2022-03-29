"""
LeetCode :: March 2022 Challenge :: 287. Find the Duplicate Number
jramaswami
"""


class Solution:
    def findDuplicate(self, nums):
        N = len(nums) - 1
        S = (N * (N+1)) // 2
        T = sum(nums)
        return T - S


def test_1():
    nums = [1,3,4,2,2]
    expected = 2
    assert Solution().findDuplicate(nums) == expected


def test_2():
    nums = [3,1,3,4,2]
    expected = 3
    assert Solution().findDuplicate(nums) == expected


def test_3():
    "WA"
    nums = [2,2,2,2,2]
    expected = 2
    assert Solution().findDuplicate(nums) == expected
