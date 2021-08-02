"""
LeetCode :: August 2021 Challenge :: Two Sum
"""


import collections


class Solution:
    def twoSum(self, nums, target):
        nums0 = collections.defaultdict(list)
        for i, n in enumerate(nums):
            nums0[n].append(i)

        for n in nums0:
            m = target - n
            if m == n:
                if len(nums0[n]) > 1:
                    return nums0[n][:2]
            elif m in nums0:
                return [nums0[n][0], nums0[m][0]]


def test_1():
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    assert Solution().twoSum(nums, target) == expected


def test_2():
    nums = [3, 2, 4]
    target = 6
    expected = [1, 2]
    assert Solution().twoSum(nums, target) == expected


def test_3():
    nums = [3, 3]
    target = 6
    expected = [0, 1]
    assert Solution().twoSum(nums, target) == expected

