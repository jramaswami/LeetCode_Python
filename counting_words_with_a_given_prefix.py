"""
LeetCode
2185. Counting Words With a Given Prefix
January 2025 Challenge
jramaswami
"""


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(x.startswith(pref) for x in words)
