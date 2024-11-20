"""
LeetCode
2516. Take K of Each Character From Left and Right
November 2024 Challenge
jramaswami

Thank You NeetCode.IO
"""


import collections
import math


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freqs = [0, 0, 0]
        for c in s:
            freqs[ord(c) - ord('a')] += 1

        # Make sure it is possible to satisfy
        if min(freqs) < k:
            return -1
        
        soln = math.inf
        left = 0
        for right, _ in enumerate(s):
            freqs[ord(s[right]) - ord('a')] -= 1
            while min(freqs) < k:
                freqs[ord(s[left]) - ord('a')] += 1
                left += 1
            soln = min(soln, len(s) - (right - left + 1))
        return soln
