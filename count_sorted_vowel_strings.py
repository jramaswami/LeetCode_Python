"""
LeetCode :: May 2022 Challenge :: 1641. Count Sorted Vowel Strings
jramaswami
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(5)]
        for r in range(5):
            dp[r][0] = 1

        for c in range(n-1):
            for r in range(5):
                for r0 in range(r, 5):
                    dp[r0][c+1] += dp[r][c]

        return sum(dp[r][-1] for r in range(5))


def test_1():
    n = 1
    expected = 5
    assert Solution().countVowelStrings(n) == expected


def test_2():
    n = 2
    expected = 15
    assert Solution().countVowelStrings(n) == expected


def test_3():
    n = 33
    expected = 66045
    assert Solution().countVowelStrings(n) == expected


def test_4():
    n = 50
    expected = 316251
    assert Solution().countVowelStrings(n) == expected