"""
LeetCode
2962. Count Subarrays Where Max Element Appears at Least K Times
March 2024 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_value = max(nums)
        max_freq = 0
        subarrays_less_than_k = 0
        window = collections.deque()
        for n in nums:
            window.append(n)
            if n == max_value:
                max_freq += 1
            while max_freq >= k:
                m = window.popleft()
                if m == max_value:
                    max_freq -= 1
            subarrays_less_than_k += len(window)

        N = len(nums)
        total_subarrays = (N * (N+1)) // 2
        return total_subarrays - subarrays_less_than_k



def test_1():
    nums = [1,3,2,3,3]
    k = 2
    expected = 6
    assert Solution().countSubarrays(nums, k) == expected


def test_2():
    nums = [1,4,2,1]
    k = 3
    expected = 0
    assert Solution().countSubarrays(nums, k) == expected