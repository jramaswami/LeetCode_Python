"""
LeetCode
1897. Redistribute Characters to Make All Strings Equal
December 2023 Challenge
jramaswami
"""


import collections
import itertools


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freqs = collections.Counter(itertools.chain(*words))
        return all(v % len(words) == 0 for v in freqs.values())