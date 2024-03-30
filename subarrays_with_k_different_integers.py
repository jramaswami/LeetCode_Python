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
        window = collections.deque()
        window_freqs = collections.defaultdict(int)
        soln = 0
        for n in nums:
            window.append(n)
            window_freqs[n] += 1
            while window and len(window_freqs) > k:
                m = window.popleft()
                window_freqs[m] -= 1
                if window_freqs[m] == 0:
                    del window_freqs[m]
            if len(window_freqs) == k:
                window_freqs0 = collections.defaultdict(int)
                for w in window:
                    soln += 1
                    window_freqs0[w] += 1
                    if window_freqs[w] == window_freqs0[w]:
                        break

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