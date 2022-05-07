"""
LeetCode :: May 2022 Challenge :: 456. 132 Pattern
jramaswami

REF: https://www.youtube.com/watch?v=XstAJdzJmVo
"""


import math


class Solution:

    def find132pattern(self, nums):
        stack = []
        curr_second_max = -math.inf
        for i in range(len(nums) - 1, -1, -1):

            # If nums[i] < curr_second_max this implies
            # nums[i] < curr_second_max < unrecorded first max
            if nums[i] < curr_second_max:
                return True

            # Find the highest number less than
            # nums[i].
            while stack and nums[i] > stack[-1]:
                curr_second_max = max(curr_second_max, stack[-1])
                stack.pop()
            stack.append(nums[i])

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