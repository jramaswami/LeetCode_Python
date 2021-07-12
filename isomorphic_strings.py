"""
LeetCode :: July 2021 Challenge :: Isomorphic Strings
jramaswami
"""


from collections import defaultdict


class Solution():
    def isIsomorphic(self, S, T):
        S_posns = defaultdict(list)
        T_posns = defaultdict(list)

        for i, c in enumerate(S):
            S_posns[c].append(i)
        for i, c in enumerate(T):
            T_posns[c].append(i)

        checked = set()
        for s, t in zip(S, T):
            if s not in checked:
                if S_posns[s] != T_posns[t]:
                    return False
                else:
                    checked.add(s)

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
