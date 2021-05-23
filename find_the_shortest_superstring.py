"""
LeetCode :: May 2021 Challenge :: Find the Shortest Superstring
jramaswami
"""
from typing import *
from itertools import combinations


def merge_strings(s1, s2):
    """Return the smallest merged string."""
    # case 1 no-overlap
    prefix_overlap = s1 + s2
    suffix_overlap = s1 + s2

    for overlap in range(1, min(len(s1), len(s2))):
        # Case 1:
        # 'catg'
        #  'atgcatc'
        if s1[-overlap:] == s2[:overlap]:
            suffix_overlap = s1[:-overlap] + s2
        # Case 2:
        #  'ctaagt'
        # 'gcta'
        if s1[:overlap] == s2[-overlap:]:
            prefix_overlap = s2[:-overlap] + s1

    if len(prefix_overlap) <= len(suffix_overlap):
        return prefix_overlap
    return suffix_overlap


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        words0 = list(words)
        while len(words0) > 1:
            print(f"{words0=}")
            best_delta = -1
            best_merge = None
            for w1, w2 in combinations(words0, 2):
                # Find the best merge
                L = len(w1) + len(w2)
                merged_word = merge_strings(w1, w2)
                delta = L - len(merged_word)
                print(f"{w1=} {w2=} {merged_word=} {delta=}")
                if delta > best_delta:
                    best_delta = delta
                    best_merge = (w1, w2, merged_word)
            print(f"{best_merge=}")
            words0.remove(best_merge[0])
            words0.remove(best_merge[1])
            words0.append(best_merge[2])

        return words0[0]


def test_merge_strings():
    assert merge_strings("loves", "leetcode") == "lovesleetcode"
    assert merge_strings("ctaagt", "gcta") == "gctaagt"
    assert merge_strings("catg", "atgcatc") == "catgcatc"

# def test_1():
#     words = ["alex","loves","leetcode"]
#     assert Solution().shortestSuperstring(words) == "alexlovesleetcode"

def test_2():
    words = ["catg","ctaagt","gcta","ttca","atgcatc"]
    assert Solution().shortestSuperstring(words) == "gctaagttcatgcatc"

def test_3():
    """WA"""
    words = ["abcdef","efde","defab"]
    assert Solution().shortestSuperstring(words) == "efdefabcdef"
