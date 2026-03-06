"""
LeetCode
1784. Check if Binary String Has at Most One Segment of Ones
March 2026 Challenge
jramaswami
"""


import itertools


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        groups = list(itertools.groupby(s, key=None))
        return sum(int(k) for k, _ in groups) == 1