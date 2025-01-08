"""
LeetCode
3042. Count Prefix and Suffix Pairs I
January 2025 Challenge
jramaswami
"""


import itertools


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        soln = 0
        for a, b in itertools.combinations(words, 2):
            if b.startswith(a) and b.endswith(a):
                soln += 1
        return soln
