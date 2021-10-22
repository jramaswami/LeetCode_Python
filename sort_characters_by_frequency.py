"""
LeetCode :: October 2021 Challenge :: 451. Sort Characters By Frequency
jramaswami
"""


import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        return "".join(c * f for c, f in sorted(ctr.items(), key=lambda t: (-t[1], t[0])))
