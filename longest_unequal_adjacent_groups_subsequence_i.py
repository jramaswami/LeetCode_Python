"""
LeetCode
2900. Longest Unequal Adjacent Groups Subsequence I
May 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        WORD, GROUP = 0, 1
        soln = []
        for w, g in zip(words, groups):
            if not soln or soln[-1][1] != g:
                soln.append((w, g))
        return [t[WORD] for t in soln]