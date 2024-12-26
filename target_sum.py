"""
LeetCode
494. Target Sum
December 2024 Challenge
jramaswami
"""


import collections
import itertools
import operator
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # BFS
        curr_queue = collections.defaultdict(int)
        curr_queue[0] = 1
        next_queue = collections.defaultdict(int)
        for n in nums:
            for a, x in curr_queue.items():
                next_queue[a - n] += x
                next_queue[a + n] += x
            curr_queue, next_queue = next_queue, collections.defaultdict(int)
        return curr_queue[target]


def test_1():
    nums = [1,1,1,1,1]
    target = 3
    expected = 5
    assert Solution().findTargetSumWays(nums, target) == expected


def test_2():
    nums = [1]
    target = 1
    expected = 1
    assert Solution().findTargetSumWays(nums, target) == expected


def test_3():
    "TLE"
    nums = [20,48,33,16,19,44,14,31,42,34,38,32,27,7,22,22,48,18,48,39]
    target = 1
    expected = 0
    assert Solution().findTargetSumWays(nums, target) == expected
