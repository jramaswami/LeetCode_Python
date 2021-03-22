"""
LeetCode :: Vowel Spellchecker
jramaswami
"""
from typing import *


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        trans = str.maketrans('aeiou', '-----')

        exact_matches = set(wordlist)
        capitalization_matches = dict()
        vowel_matches = dict()
        for w in wordlist:
            w0 = w.lower()
            w1 = w0.translate(trans)
            if w0 not in capitalization_matches:
                capitalization_matches[w0] = w
            if w1 not in vowel_matches:
                vowel_matches[w1] = w

        def query(word):
            word_l = word.lower()
            word_t = word_l.translate(trans)
            if word in exact_matches:
                return word
            elif word_l in capitalization_matches:
                return capitalization_matches[word_l]
            elif word_t in vowel_matches:
                return vowel_matches[word_t]
            else:
                return ""

        return [query(q) for q in queries]


def test_1():
    wordlist = ["KiTe","kite","hare","Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    expected = ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
    result = Solution().spellchecker(wordlist, queries)
    assert result == expected
