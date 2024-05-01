"""
LeetCode
2000. Reverse Prefix of Word
May 2024 Challenge
jramaswami
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        return word[0:i+1][::-1] + word[i+1:]