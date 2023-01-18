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

        def kadane(X):
            result = -math.inf
            curr_sum = 0
            for x in X:
                curr_sum = max(x, curr_sum + x)
                result = max(curr_sum, result)
            return result

        soln = -math.inf
        A0 = collections.deque(A)
        for _ in range(len(A0)):
            soln = max(soln, kadane(A0))
            A0.rotate(-1)
        return soln



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