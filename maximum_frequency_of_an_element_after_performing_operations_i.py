"""
LeetCode
3346. Maximum Frequency of an Element After Performing Operations I
October 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        soln = 0
        window = collections.deque()
        window_freqs = collections.defaultdict(int)
        i = 0
        low = min(nums)
        high = max(nums)
        for x in range(low, high+1):
            # Add more values to window as long as they are <= x + k
            while i < len(nums) and nums[i] <= x + k:
                window.append(nums[i])
                window_freqs[nums[i]] += 1
                i += 1
            # Remove any values in window that are < x - k
            while window and window[0] < x - k:
                window_freqs[window[0]] -= 1
                window.popleft()
            # Count how many values we can make equal to x
            same = window_freqs[x]
            in_range = len(window) - same
            soln = max(soln, same + min(in_range, numOperations))

        return soln