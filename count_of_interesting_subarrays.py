"""
LeetCode
2845. Count of Interesting Subarrays
April 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        soln = 0
        # Convert nums yes/no for nums[i] % modulo == k
        nums0 = [1 if n % modulo == k else 0 for n in nums]
        for left, _ in enumerate(nums0):
            cnt = 0
            for right, x in enumerate(nums0[left:]):
                cnt += x
                if cnt % modulo == k:
                    soln += 1
        return soln


def test_1():
    nums = [3,2,4]
    modulo = 2
    k = 1
    expected = 3
    assert Solution().countInterestingSubarrays(nums, modulo, k) == expected
