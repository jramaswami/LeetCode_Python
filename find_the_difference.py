"""
LeetCode :: February 2022 Challenge :: 389. Find the Difference
jramaswami
"""


import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ctr_s = collections.Counter(s)
        ctr_t = collections.Counter(t)

        for k in ctr_t:
            if k not in ctr_s or ctr_t[k] > ctr_s[k]:
                return k
