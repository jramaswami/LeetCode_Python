"""
LeetCode :: October 2021 Challenge :: 1044. Longest Duplicate Substring
jramaswami
"""


class Solution:
    def longestDupSubstring(self, S):

        def lds(i, j):
            result = 0
            while i < len(S) and j < len(S):
                if S[i] != S[j]:
                    return result
                result += 1
                i += 1
                j += 1
            return result

        soln_length = 0
        soln = ""
        for i, _ in enumerate(S):
            for j, _ in enumerate(S[i+1:], start=i+1):
                k = lds(i, j)
                if k > soln_length:
                    soln_length = k
                    soln = S[i:i+k]
        return soln


def test_1():
    S = "banana"
    expected = "ana"
    assert Solution().longestDupSubstring(S) == expected


def test_2():
    S = "abcd"
    expected = ""
    assert Solution().longestDupSubstring(S) == expected
