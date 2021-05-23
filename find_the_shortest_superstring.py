"""
LeetCode :: May 2021 Challenge :: Find the Shortest Superstring
jramaswami

Thank you Larry!
"""
from typing import *
from math import inf


def merge_cost(w1, w2):
    """Return the cost of merging w2 after w1."""
    for k in range(len(w2), 0, -1):
        if w1.endswith(w2[0:k]):
            return k
    return 0


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:

        words0 = list(words)

        # The cost of appending w2 after w1
        cost = [[inf for _ in words0] for _ in words0]
        for i, w1 in enumerate(words0):
            for j, w2 in enumerate(words0):
                if i == j:
                    continue
                cost[i][j] = merge_cost(w1, w2)


        cache = dict()
        # Gets the best word where the last word is index and mask is still
        # contains items able to be used.

        # Adding i to some other string ...
        def get_subset(i, mask):
            wd1 = words0[i]

            # print(f"get_subset({i=} mask={mask:013b}) {wd1=}")
            # If no other strings have been used, then I cannot overlap.
            if mask == 0:
                return wd1

            key = (i, mask)
            if key in cache:
                return cache[key]

            soln = ""
            best_length = inf
            for j, wd2 in enumerate(words0):
                # Get me the best word starting with if it is in my mask.
                if (mask & (1 << j)) > 0:
                    # What is the cost of appending a word starting with wd2?
                    c = cost[i][j]
                    # Get the best word that does not include me.
                    mask0 = mask ^ (1 << j)
                    r = get_subset(j, mask0)
                    # r is the best word that starts with wd2, remove the
                    # overalp from wd2 and then append it to wd1

                    current = wd1 + r[c:]
                    # print(f"\t{wd1=} {i=} {wd2=} {j=} {r=} {c=} {current=} {soln=} {words0=}")
                    if len(current) < best_length:
                        best_length = len(current)
                        soln = current

            cache[key] = soln
            return soln

        best_word = ""
        best_length = inf
        all_bits = (1 << len(words0)) - 1
        # print(f"{all_bits:013b} {len(words0)=}")
        for i, start_word in enumerate(words0):
            mask = all_bits ^ (1 << i)
            curr = get_subset(i, mask)
            # print(f"{start_word=}, {curr=} {mask:013b}")
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
    assert Solution().shortestSuperstring(words) == "efdefabcdef"
