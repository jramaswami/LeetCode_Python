"""
LeetCode :: October 2022 Challenge :: 3Sum Closest
jramaswami
"""


import math
import bisect


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        soln = math.inf
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start=i+1):
                d = target - a - b
                k = bisect.bisect_right(nums, d)
                if k > 0 and k - 1 != i and k - 1 != j:
                    t = a + b + nums[k-1]
                    if abs(target - t) < abs(target - soln):
                        soln = t
                if k < len(nums) and k != i and k != j:
                    t = a + b + nums[k]
                    if abs(target - t) < abs(target - soln):
                        soln = t
        return soln


def test_1():
    nums = [-1,2,1,-4]
    target = 1
    assert Solution().threeSumClosest(nums, target) == 2


def test_2():
    nums = [0, 0, 0]
    target = 0
    assert Solution().threeSumClosest(nums, target) == 0