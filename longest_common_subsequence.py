"""
LeetCode
1143. Longest Common Subsequence
December 2022 Challenge
jramaswami
"""


import functools


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        @functools.cache
        def rec(i, j):
            if i >= len(text1):
                return 0
            if j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + rec(i+1, j+1)
            return max(rec(i+1, j), rec(i, j+1))

        return rec(0, 0)


def test_1():
    text1 = "abcde"
    text2 = "ace"
    expected = 3
    assert Solution().longestCommonSubsequence(text1, text2) == expected


def test_2():
    text1 = "abc"
    text2 = "abc"
    expected = 3
    assert Solution().longestCommonSubsequence(text1, text2) == expected


def test_3():
    text1 = "abc"
    text2 = "def"
    expected = 0
    assert Solution().longestCommonSubsequence(text1, text2) == expected


def main():
    """Main program."""
    # Timing
    import string
    import random
    import sys
    sys.setrecursionlimit(pow(10, 9))
    text1 = "".join(random.choice(string.ascii_lowercase) for _ in range(1000))
    text2 = "".join(random.choice(string.ascii_lowercase) for _ in range(1000))
    print(text1)
    print(text2)
    print(Solution().longestCommonSubsequence(text1, text2))


if __name__ == '__main__':
    main()
