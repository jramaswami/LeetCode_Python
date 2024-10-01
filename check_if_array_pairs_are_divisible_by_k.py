"""
LeetCode
1497. Check If Array Pairs Are Divisible by k
October 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freqs = collections.Counter(t % k for t in arr)
        for t in freqs:
            if t == 0 and (freqs[t] % 2) != 0:
                return False
            if t > 0 and freqs[t] != freqs[k-t]:
                return False
        return True
