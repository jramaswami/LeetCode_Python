"""
LeetCode
1027. longest arithmetic subsequence
june 2023 challenge
jramaswami
"""


import collections
import functools
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        nearest_deltas = [dict() for _ in nums]
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start=i+1):
                delta = b - a
                if delta not in nearest_deltas[i]:
                    nearest_deltas[i][delta] = j

        @functools.cache
        def rec(i, delta):
            if delta in nearest_deltas[i]:
                return 1 + rec(nearest_deltas[i][delta], delta)
            return 1

        soln = 2
        for i, _ in enumerate(nums):
            for delta in nearest_deltas[i]:
                soln = max(soln, rec(i, delta))
        return soln


def test_1():
    nums = [3,6,9,12]
    expected = 4
    assert Solution().longestArithSeqLength(nums) == expected


def test_2():
    nums = [9,4,7,2,10]
    expected = 3
    assert Solution().longestArithSeqLength(nums) == expected


def test_3():
    nums = [20,1,15,3,10,5,8]
    expected = 4
    assert Solution().longestArithSeqLength(nums) == expected
