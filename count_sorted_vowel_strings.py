"""
LeetCode :: May 2022 Challenge :: 1641. Count Sorted Vowel Strings
jramaswami
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:

            vowels = "aeiou"

            def solve(i, p):
                if i >= n:
                    return 1

                # With each letter >= prev
                return sum(solve(i+1, v) for v, _ in enumerate(vowels[p:], start=p))

            return solve(0, 0)


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