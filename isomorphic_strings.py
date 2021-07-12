"""
LeetCode :: July 2021 Challenge :: Isomorphic Strings
jramaswami
"""


from collections import defaultdict


class Solution():
    def isIsomorphic(self, S, T):
        map_s_to_t = dict()
        map_t_to_s = dict()
        for s, t in zip(S, T):
            if map_s_to_t.setdefault(s, t) != t or map_t_to_s.setdefault(t, s) != s:
                return False
        return True


def test_1():
    S = "egg"
    T = "add"
    assert Solution().isIsomorphic(S, T) == True


def test_2():
    S = "foo"
    T = "bar"
    assert Solution().isIsomorphic(S, T) == False


def test_3():
    S = "paper"
    T = "title"
    assert Solution().isIsomorphic(S, T) == True


def test_4():
    """WA"""
    S = "bbbaaaba"
    T = "aaabbbba"
    assert Solution().isIsomorphic(S, T) == False


def test_5():
    """WA"""
    S = "badc"
    T = "baba"
    assert Solution().isIsomorphic(S, T) == False
