"""
LeetCode :: September 2021 Challenge :: Distinct Subsequences
jramaswami
"""


def solve(i, j, S, T):
    # Base case: we have found and consumed all letters of the target word.
    if j >= len(T):
        return 1
    # Base case: we have exhausted the letters of our haystack without finding
    # the target word.
    if i >= len(S):
        return 0

    # If the letter at S[i] is the letter as T[j], we can consume the letter
    # and advance both i and j.
    result = 0
    if S[i] == T[j]:
        result += solve(i + 1, j + 1, S, T)

    # We can ignore the current letter at S[i] and advance i.
    result += solve(i + 1, j, S, T)
    return result


class Solution:

    def numDistinct(self, S, T):
        return solve(0, 0, S, T)


def test_1():
    S = "rabbbit"
    T = "rabbit"
    expected = 3
    assert Solution().numDistinct(S, T) == expected


def test_2():
    S = "babgbag"
    T = "bag"
    expected = 5
    assert Solution().numDistinct(S, T) == expected


def test_3():
    """TLE"""
    S = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
    T = "bddabdcae"
    expected = 5
    assert Solution().numDistinct(S, T) == expected
