"""
LeetCode :: May 2022 Challenge Shortest Unsorted Continuous Subarray
jramaswami
"""


from typing import *
import itertools
import math


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_to_left = list(itertools.accumulate(nums, max))
        min_to_right = list(reversed(list(itertools.accumulate(reversed(nums), min))))
        left = math.inf
        right = -math.inf
        for i, (n, mn, mx) in enumerate(zip(nums, min_to_right, max_to_left)):
            if n != mn or n != mx:
                left = min(left, i)
                right = max(right, i)

        if left < len(nums):
            return right - left + 1
        return 0



def test_1():
    nums = [2,6,4,8,10,9,15]
    assert Solution().findUnsortedSubarray(nums) == 5


def test_2():
    nums = [1,2,3,4]
    assert Solution().findUnsortedSubarray(nums) == 0


def test_3():
    nums = [1]
    assert Solution().findUnsortedSubarray(nums) == 0


def test_4():
    nums = [4,3,2,1]
    assert Solution().findUnsortedSubarray(nums) == 4


def test_5():
    nums = [1,3,2,2,2]
    assert Solution().findUnsortedSubarray(nums) == 4


def test_6():
    nums = [2,1]
    assert Solution().findUnsortedSubarray(nums) == 2


def test_7():
    nums = [2,3,3,2,4]
    assert Solution().findUnsortedSubarray(nums) == 3


def test_8():
    nums = [1,2,4,5,3]
    assert Solution().findUnsortedSubarray(nums) == 3
