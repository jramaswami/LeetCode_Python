"""
LeetCode
2840. Check if Strings Can be Made Equal With Operations II
March 2026 Challenge
jramaswami
"""


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        a = tuple(sorted(c for c in s1[::2]))
        b = tuple(sorted(c for c in s1[1::2]))
        x = tuple(sorted(c for c in s2[::2]))
        y = tuple(sorted(c for c in s2[1::2]))
        return a == x and b == y