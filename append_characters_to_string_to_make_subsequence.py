"""
LeetCode
2486. Append Characters to String to Make Subsequence
June 2024 Challenge
jramaswami
"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for j, _ in enumerate(s):
            if i < len(t) and s[j] == t[i]:
                i += 1
        return len(t) - i
