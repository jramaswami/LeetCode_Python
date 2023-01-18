"""
LeetCode
918. Maximum Sum Circular Subarray
January 2023 Challenge
jramaswami
"""


import collections
import math
from typing import *


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total = curr_max = curr_min = 0
        max_sum = -math.inf
        min_sum = math.inf

        for a in A:
            total += a
            curr_max = max(curr_max + a, a)
            curr_min = min(curr_min + a, a)
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)
        return max_sum if max_sum < 0 else max(max_sum, total - min_sum)



def test_1():
    nums = [1,-2,3,-2]
    expected = 3
    assert Solution().maxSubarraySumCircular(nums) == expected


def test_2():
    nums = [5,-3,5]
    expected = 10
    assert Solution().maxSubarraySumCircular(nums) == expected


def test_3():
    nums = [-3,-2,-3]
    expected = -2
    assert Solution().maxSubarraySumCircular(nums) == expected


def test_4():
    "WA"
    nums = [3,-1,2,-1]
    expected = 4
    assert Solution().maxSubarraySumCircular(nums) == expected