"""
LeetCode :: March 2022 Challenge :: 392. Is Subsequence
jramaswami
"""


class Solution:

    def isSubsequence(self, S, T):
        i = 0
        for j, _ in enumerate(T):
            if i < len(S) and S[i] == T[j]:
                i += 1
        return i >= len(S)



def test_1():
    s = "abc"
    t = "ahbgdc"
    expected = True
    assert Solution().isSubsequence(s, t) == expected


def test_2():
    s = "axc"
    t = "ahbgdc"
    expected = False
    assert Solution().isSubsequence(s, t) == expected
