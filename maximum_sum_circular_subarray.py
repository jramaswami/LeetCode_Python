"""
LeetCode
918. Maximum Sum Circular Subarray
January 2023 Challenge
jramaswami
"""



import itertools as it
import collections
from typing import *


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        soln = max(A) # non-empty
        curr_sum = 0
        window = collections.deque()
        for x in it.chain.from_iterable(it.repeat(A, 2)):
            if x < 0:
                curr_sum = 0
                window = []
            else:
                curr_sum += x
                window.append(x)
                while len(window) > len(A):
                    curr_sum -= window[0]
                    window.popleft()
                soln = max(soln, curr_sum)
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
    nums = [-3,-2,-3]
    expected = 3
    assert Solution().maxSubarraySumCircular(nums) == expected