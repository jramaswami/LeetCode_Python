"""
LeetCode
2845. Count of Interesting Subarrays
April 2025 Challenge
jramaswami
"""


import collections
import itertools
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        soln = 0
        # Convert nums yes/no for nums[i] % modulo == k
        nums0 = [1 if n % modulo == k else 0 for n in nums]
        # Prefix sums for the number of nums[i] % modulo == k
        nums1 = [x % modulo for x in itertools.accumulate(nums0)]
        seen = collections.defaultdict(int)
        seen[0] = 1
        for x in nums1:
            soln += seen[x]
            seen[x] += 1
        return soln


def test_1():
    nums = [3,2,4]
    modulo = 2
    k = 1
    expected = 3
    assert Solution().countInterestingSubarrays(nums, modulo, k) == expected



def test_2():
    nums = [3,1,9,6]
    modulo = 3
    k = 0
    expected = 2
    assert Solution().countInterestingSubarrays(nums, modulo, k) == expected


def test_3():
    nums = [9, 75, 78, 50, 66, 44, 83, 23, 7, 65, 98, 76, 39, 80, 43, 88, 86, 91, 97, 4]
    modulo = 3
    k = 0
    expected = 75
    assert Solution().countInterestingSubarrays(nums, modulo, k) == expected


def test_4():
    "WA"
    nums = [11,12,21,31]
    modulo = 10
    k = 1
    expected = 5
    assert Solution().countInterestingSubarrays(nums, modulo, k) == expected
