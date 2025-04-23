"""
LeetCode
1399. Count Largest Group
April 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def countLargestGroup(self, n: int) -> int:

        def digit_sum(x):
            result = 0
            while x:
                x, r = divmod(x, 10)
                result += r
            return result

        digit_sums = [digit_sum(x) for x in range(1,n+1)]
        freqs = collections.Counter(digit_sums)
        max_freq = max(freqs.values())
        return sum(1 if freqs[x] == max_freq else 0 for x in freqs)


def test_1():
    n = 13
    expected = 4
    assert Solution().countLargestGroup(n) == expected


def test_2():
    n = 2
    expected = 2
    assert Solution().countLargestGroup(n) == expected
