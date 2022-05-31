"""
LeetCode :: Grind 75 :: Two Sum
"""


class Solution:
    def twoSum(self, nums, target):
        prevs = dict()
        for i, n in enumerate(nums):
            d = target - n
            if d in prevs:
                return [min(i, prevs[d]), max(i, prevs[d])]
            prevs[n] = i



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
