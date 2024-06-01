"""
LeetCode
3110. Score of a String
June 2024 Challenge
jramaswami
"""


class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(a) - ord(b)) for a, b in zip(s[:-1], s[1:]))
