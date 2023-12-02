"""
LeetCode
1160. Find Words That Can Be Formed by Characters
December 2023 Challenge
jramaswami
"""


from typing import List
import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = collections.Counter(chars)
        soln = 0
        for word in words:
            word_counter = collections.Counter(word)
            if all(word_counter[k] <= chars_counter.get(k, 0) for k in word_counter):
                soln += len(word)
        return soln