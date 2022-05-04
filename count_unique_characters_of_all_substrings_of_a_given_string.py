"""
LeetCode :: 828. Count Unique Characters of All Substrings of a Given String
jramaswami
"""


import string


MOD = pow(10, 9) + 7


class Solution:

    def uniqueLetterString(self, S):
        # Hold all the indexes for S (one-based).
        indexes = {c: [0] for c in string.ascii_uppercase}
        for i, c in enumerate(S):
            indexes[c].append(i+1)
        for c in string.ascii_uppercase:
            indexes[c].append(len(S)+1)

        soln = 0
        # For each index, count the number of substrings for which S[i] will
        # be the only occurrence of that letter.
        for c in string.ascii_uppercase:
            if len(indexes[c]) > 2:
                for i in range(1, len(indexes[c])-1):
                    left = (indexes[c][i] - indexes[c][i-1])
                    right = (indexes[c][i+1] - indexes[c][i])
                    k = (left * right) % MOD
                    soln = (soln + k) % MOD
        return soln


def test_1():
    s = "ABC"
    expected = 10
    assert Solution().uniqueLetterString(s) == expected


def test_2():
    s = "ABA"
    expected = 8
    assert Solution().uniqueLetterString(s) == expected


def test_3():
    s = "LEETCODE"
    expected = 92
    assert Solution().uniqueLetterString(s) == expected