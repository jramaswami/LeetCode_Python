"""
LeetCode :: August 2021 Challenge :: Palindrome Partitioning II
jramaswami
"""


import collections


class Solution:
    def minCut(self, S):
        # The maximum number of cuts is len(S) - 1.
        dp = collections.defaultdict(lambda: len(S) - 1)
        dp[-1] = -1

        for i, _ in enumerate(S):
            freqs = collections.defaultdict(int)
            odd_freqs = 0
            for j, c in enumerate(S[i:], start=i):
                freqs[c] += 1
                if freqs[c] % 2:
                    odd_freqs += 1
                else:
                    odd_freqs -= 1

                if odd_freqs <= 1 and S[i:j+1] == S[i:j+1][::-1]:
                    # A palindrome exists from S[i:j+1]
                    dp[j] = min(dp[j], dp[i-1] + 1)

        return dp[len(S)-1]


def test_1():
    S = "aab"
    expected = 1
    assert Solution().minCut(S) == expected


def test_2():
    S = "a"
    expected = 0
    assert Solution().minCut(S) == expected


def test_3():
    S = "ab"
    expected = 1
    assert Solution().minCut(S) == expected


def test_4():
    S = "aaaaabbbb"
    expected = 1
    assert Solution().minCut(S) == expected


def test_5():
    S = "bbacbcabbaabaccbacba"
    expected = 8
    assert Solution().minCut(S) == expected
