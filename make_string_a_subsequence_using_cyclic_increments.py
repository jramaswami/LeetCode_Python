"""
LeetCode
2825. Make String a Subsequence Using Cyclic Increments
December 2024 Challenge
jramaswami
"""


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def operation(char):
            x = ord(char) - ord('a')
            x += 1
            x %= 26
            c = chr(x + ord('a'))
            return c
        
        j = 0
        for c in str1:
            if j < len(str2) and (c == str2[j] or operation(c) == str2[j]):
                j += 1
        return j >= len(str2)
