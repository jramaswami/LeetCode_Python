"""
LeetCode
2914. Minimum Number of Changes to Make Binary String Beautiful
November 2024 Challenge
jramaswami
"""


class Solution:
    def minChanges(self, s: str) -> int:
        soln = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i+1]:
                soln += 1
        return soln
