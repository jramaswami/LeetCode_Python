"""
LeetCode :: October 2021 Challenge :: 1143. Longest Common Subsequence
jramaswami
"""


from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        @lru_cache(maxsize=None)
        def lcs(i, j):
            # Base case.
            if i < 0 or j < 0:
                return 0
            # Case 1: equals letters
            if text1[i] == text2[j]:
                return lcs(i - 1, j - 1) + 1
            # Case 2: non-equal letters
            return max(lcs(i, j - 1), lcs(i - 1, j))

        return lcs(len(text1) - 1, len(text2) - 1)


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
