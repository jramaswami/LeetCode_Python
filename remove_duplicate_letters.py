"""
LeetCode :: March 2022 Challenge :: 316. Remove Duplicate Letters
jramaswami
"""


class Solution:
    def removeDuplicateLetters(self, S):
        last_index = dict()
        for i, c in enumerate(S):
            last_index[c] = i

        T = []
        i = 0
        while len(T) < len(last_index):
            j = min(last_index.values())
            c, k = min((y, x) for x, y in enumerate(S[i:j+1], start=i) if last_index[y] < len(S))
            last_index[c] = len(S)
            T.append(c)
            i = k+1
        return "".join(T)


def test_1():
    s = "bcabc"
    expected = "abc"
    assert Solution().removeDuplicateLetters(s) == expected


def test_2():
    s = "cbacdcbc"
    expected = "acdb"
    assert Solution().removeDuplicateLetters(s) == expected


def test_3():
    s = ""
    expected = ""
    assert Solution().removeDuplicateLetters(s) == expected
