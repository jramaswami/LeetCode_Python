"""
LeetCode
2958. Length of Longest Subarray With at Most K Frequency
March 2023 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freqs = collections.defaultdict(int)
        window = collections.deque()
        soln = 0
        for n in nums:
            freqs[n] += 1
            window.append(n)
            while window and freqs[n] > k:
                m = window.popleft()
                freqs[m] -= 1
            soln = max(soln, len(window))
        return soln


def test_1():
    nums = [1,2,3,1,2,3,1,2]
    k = 2
    expected = 6
    assert Solution().maxSubarrayLength(nums, k) == expected


def test_2():
    nums = [1,2,1,2,1,2,1,2]
    k = 1
    expected = 2
    assert Solution().maxSubarrayLength(nums, k) == expected


def test_3():
    nums = [5,5,5,5,5,5,5]
    k = 4
    expected = 4
    assert Solution().maxSubarrayLength(nums, k) == expected