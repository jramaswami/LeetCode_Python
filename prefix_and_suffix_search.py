"""
Leet Code :: May 2021 Challenge :: Prefix and Suffix Search
jramaswami

Thank you Larry!
"""
from typing import *
from collections import defaultdict
from functools import lru_cache


class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)

        for index, word in enumerate(words):
            rword = word[::-1]
            for i in range(1, len(word) + 1):
                self.prefixes[word[:i]].add(index)
                self.suffixes[rword[:i]].add(index)

    @lru_cache(maxsize=None)
    def f(self, prefix: str, suffix: str) -> int:
        possibles = self.prefixes[prefix] & self.suffixes[suffix[::-1]]
        if possibles:
            return (max((len(self.words[i]), i) for i in possibles))[1]
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


def test_1():
    methods = ["WordFilter", "f"]
    arguments = [[["apple"]], ["a", "e"]]
    wf = WordFilter(*arguments[0])
    expected = [None, 0]
    for meth, args, exp in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(wf, meth)(*args) == exp


def test_2():
    methods = ["WordFilter", "f", "f", "f"]
    arguments = [[["apple", "orange", "oe", "orangeorangeorange"]], ["a", "e"],["orange", "orange"], ["app", "zle"]]
    wf = WordFilter(*arguments[0])
    expected = [None, 0, 3, -1]
    for meth, args, exp in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(wf, meth)(*args) == exp



def test_3():
    """WA"""
    methods = ["WordFilter","f","f","f","f","f","f","f","f","f","f"]
    arguments = [[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]
    wf = WordFilter(*arguments[0])
    expected = [None,9,4,5,0,8,1,2,5,3,1]
    for meth, args, exp in zip(methods[1:], arguments[1:], expected[1:]):
        print(meth, args, exp)
        assert getattr(wf, meth)(*args) == exp