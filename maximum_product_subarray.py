"""
LeetCode :: December 2021 Challenge :: 152. Maximum Product Subarray
jramaswami
"""


import math


class Solution:
    def maxProduct(self, nums):
        curr = 1
        prefix = []
        soln = -math.inf
        for n in nums:
            curr *= n
            prefix.append(curr)

        for left, _ in enumerate(prefix):
            for right, P in enumerate(prefix[left:], start=left):
                if left == right:
                    soln = max(soln, nums[left])
                elif left == 0:
                    soln = max(soln, P)
                else:
                    if prefix[left - 1] != 0:
                        soln = max(soln, P // prefix[left - 1])
        return soln



def test_1():
    nums = [2,3,-2,4]
    expected = 6
    assert Solution().maxProduct(nums) == expected


def test_2():
    nums = [-2,0,-1]
    expected = 0
    assert Solution().maxProduct(nums) == expected


def test_3():
    nums = [-8, -6, -5, -10, 9, -9, 2, -2, 9, 0, 6, -4, 3, -2, -10, 10]
    expected = 6998400
    assert Solution().maxProduct(nums) == expected


def test_4():
    "WA"
    nums = [-2]
    expected = -2
    assert Solution().maxProduct(nums) == expected


def test_5():
    "WA"
    nums = [1,0,-1,2,3,-5,-2]
    expected = 60
    assert Solution().maxProduct(nums) == expected
