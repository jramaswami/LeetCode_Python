"""
LeetCode
2302. Count Subarrays With Score Less Than K
April 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        window = collections.deque()
        curr_sum = 0
        soln = 0
        for x in nums:
            window.append(x)
            curr_sum += x
            while curr_sum * len(window) >= k:
                y = window.popleft()
                curr_sum -= y
            if window:
                soln += len(window)
        return soln


def test_1():
    nums = [2,1,4,3,5]
    k = 10
    expected = 6
    assert Solution().countSubarrays(nums, k) == expected
