"""
LeetCode
2273. Find Resultant Array After Removing Anagrams
October 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        WORD, KEY = 0, 1
        stack = []
        for wd in words:
            key = ''.join(sorted(wd))
            if not stack or stack[-1][KEY] != key:
                stack.append((wd, key))
        return [t[WORD] for t in stack]