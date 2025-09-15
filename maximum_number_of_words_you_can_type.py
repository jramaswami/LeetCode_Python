"""
LeetCode
1935. Maximum Number of Words You Can Type
September 2025 Challenge
jramaswami
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_letters = set(brokenLetters)
        return sum(
            0 if any(c in broken_letters for c in wd) else 1
            for wd in text.split()
        )
