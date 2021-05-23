"""
LeetCode :: May 2021 Challenge :: Find the Shortest Superstring
jramaswami

Thank you Larry!
"""
from typing import *
from math import inf
from functools import lru_cache


def merge_cost(w1, w2):
    """Return the cost of merging w2 after w1."""
    for k in range(len(w2), 0, -1):
        if w1.endswith(w2[0:k]):
            return k
    return 0


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        # The cost of appending w2 after w1 where the cost is the number
        # of letters to be removed from w2 to make the merge.
        cost = [[inf for _ in words] for _ in words]
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i == j:
                    continue
                cost[i][j] = merge_cost(w1, w2)

        # Adding i to some other string ...
        @lru_cache(maxsize=None)
        def get_subset(i, mask):
            """
            Return the best string merging words[i] to the remaining unmerged
            words.  In the mask, if a bit is set, then the word is available
            to be merged.
            """
            wd1 = words[i]

            # If no other strings have been used, then I cannot overlap, so
            # just return me as the word.
            if mask == 0:
                return wd1

            soln = ""
            best_length = inf
            for j, wd2 in enumerate(words):
                # Get me the best merged word starting with wd2 if wd2 is
                # available for merging.
                if (mask & (1 << j)) > 0:
                    # Get the cost for the merging wd2.
                    c = cost[i][j]
                    # Get the best word that does not include wd2.
                    mask0 = mask ^ (1 << j)
                    r = get_subset(j, mask0)
                    # Remove the overlap between wd1 and r (which starts with
                    # wd2, then merge r with wd1.
                    current = wd1 + r[c:]
                    # Keep track of the smalled possible word.
                    if len(current) < best_length:
                        best_length = len(current)
                        soln = current
            # Return the smallest possible word that starts with wd1
            return soln

        # Give each word the chance to be the first word.
        best_word = ""
        best_length = inf
        all_bits = (1 << len(words)) - 1
        for i, start_word in enumerate(words):
            mask = all_bits ^ (1 << i)
            curr = get_subset(i, mask)
            if len(curr) < best_length:
                best_length = len(curr)
                best_word = curr
        return best_word


def test_1():
    words = ["alex","loves","leetcode"]
    assert Solution().shortestSuperstring(words) == "alexlovesleetcode"


def test_2():
    words = ["catg","ctaagt","gcta","ttca","atgcatc"]
    assert Solution().shortestSuperstring(words) == "gctaagttcatgcatc"


def test_3():
    """WA"""
    words = ["abcdef","efde","defab"]
    # assert Solution().shortestSuperstring(words) == "efdefabcdef"
    # Different solution from expected but valid.
    assert Solution().shortestSuperstring(words) == "abcdefdefab"
