"""
LeetCode
2053. Kth Distinct String in an Array
August 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freqs = collections.Counter(arr)
        i = 0
        for x in arr:
            if freqs[x] == 1:
                i += 1
                if i == k:
                    return x
        return ""