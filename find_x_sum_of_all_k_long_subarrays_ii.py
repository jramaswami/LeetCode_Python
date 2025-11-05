"""
LeetCode
3318. Find X-Sum of All K-Long Subarrays II
November 2025 Challenge
jramaswami
"""


import collections
from typing import List
from sortedcontainers import SortedSet


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        soln = []
        freqs = collections.Counter()
        window = collections.deque()
        window_freqs = SortedSet()
        for n in nums:
            if freqs[n] > 0:
                old_key = (freqs[n], n)
                window_freqs.remove(old_key)
            freqs[n] += 1
            window.append(n)
            new_key = (freqs[n], n)
            window_freqs.add(new_key)

            while len(window) > k:
                old_key = (freqs[window[0]], window[0])
                window_freqs.remove(old_key)
                freqs[window[0]] -= 1
                if freqs[window[0]] > 0:
                    new_key = (freqs[window[0]], window[0])
                    window_freqs.add(new_key)
                window.popleft()

            if len(window) == k:
                soln.append(sum(f * v for f, v in window_freqs[-x:]))

        return soln