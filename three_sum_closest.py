"""
LeetCode :: October 2022 Challenge :: 3Sum Closest
jramaswami

Thank You Larry!
"""


import math


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        soln = math.inf
        for i, _ in enumerate(nums):
            left, right = i+1, len(nums)-1
            while left < right:
                t = nums[i] + nums[left] + nums[right]
                if abs(target - t) < abs(target - soln):
                    soln = t
                if t > target:
                    right -= 1
                else:
                    left += 1
        return soln


def test_1():
    nums = [-1,2,1,-4]
    target = 1
    assert Solution().threeSumClosest(nums, target) == 2


def test_2():
    nums = [0, 0, 0]
    target = 0
    assert Solution().threeSumClosest(nums, target) == 0