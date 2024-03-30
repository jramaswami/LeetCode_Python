"""
LeetCode
992. Subarrays with K Different Integers
March 2023 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        soln = 0
        for length in range(1, len(nums) + 1):
            # Initialize window
            window = collections.deque()
            window_freqs = collections.defaultdict(int)
            i = 0
            while len(window) < length:
                n = nums[i]
                window.append(n)
                window_freqs[n] += 1
                i += 1
            if len(window_freqs) == k:
                soln += 1
            while i < len(nums):
                m = window.popleft()
                window_freqs[m] -= 1
                n = nums[i]
                window.append(n)
                window_freqs[n] += 1
                if n != m and window_freqs[m] == 0:
                    del window_freqs[m]
                if len(window_freqs) == k:
                    soln += 1
                i += 1
        return soln


def test_1():
    nums = [1,2,1,2,3]
    k = 2
    expected = 7
    assert Solution().subarraysWithKDistinct(nums, k) == expected


def test_2():
    nums = [1,2,1,3,4]
    k = 3
    expected = 3
    assert Solution().subarraysWithKDistinct(nums, k) == expected


def test_large():
    nums = [1 for _ in range(2 * pow(10,4))]
    k = 1
    expected = len(nums)
    assert Solution().subarraysWithKDistinct(nums, k) == expected