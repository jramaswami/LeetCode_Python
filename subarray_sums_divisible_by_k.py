"""
LeetCode
974. Subarray Sums Divisible by K
January 2023 Challenge
jramaswami
"""


import collections
from typing import *


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        previous_sums = collections.defaultdict(int)
        current_sum = soln = 0
        previous_sums[0] += 1
        for n in nums:
            current_sum = (current_sum + n) % k
            soln += previous_sums[current_sum]
            previous_sums[current_sum] += 1
        return soln


def test_1():
    nums = [4,5,0,-2,-3,1]
    k = 5
    expected = 7
    assert Solution().subarraysDivByK(nums, k) == expected


def test_2():
    nums = [5]
    k = 9
    expected = 0
    assert Solution().subarraysDivByK(nums, k) == expected