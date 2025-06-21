"""
LeetCode
3085. Minimum Deletions to Make String K-Special
June 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        INF = pow(10, 10)
        soln = INF
        freqs = collections.Counter(word)
        for root in freqs:
            deletions = 0
            minimum_count = freqs[root]
            for count in freqs.values():
                if count < minimum_count:
                    deletions += count
                if count > minimum_count + k:
                    deletions += (count - minimum_count - k)
            soln = min(soln, deletions)
        return soln


def test_1():
    word = "aabcaba"
    k = 0
    expected = 3
    assert Solution().minimumDeletions(word, k) == expected


def test_2():
    word = "dabdcbdcdcd"
    k = 2
    expected = 2
    assert Solution().minimumDeletions(word, k) == expected