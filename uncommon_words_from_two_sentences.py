"""
LeetCode
884. Uncommon Words from Two Sentences
September 2024 Challenge
jramaswami
"""


import itertools
import collections


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # If the word is uncommon, it only appears once in both sentences combined
        ctr = collections.Counter(itertools.chain(s1.split(), s2.split()))
        return [wd for wd in ctr if ctr[wd] == 1]
