"""
LeetCode
3318. Find X-Sum of All K-Long Subarrays II
November 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        soln = []
        freqs = collections.Counter()
        window = collections.deque()
        for n in nums:
            freqs[n] += 1
            window.append(n)

            while len(window) > k:
                freqs[window[0]] -= 1
                window.popleft()

            if len(window) == k:
                A = list(sorted(((f, v) for v, f in freqs.items()), reverse=True))
                soln.append(sum(f * v for f, v in A[:x]))

        return soln