"""
LeetCode :: May 2022 Challenge :: 1679. Max Number of K-Sum Pairs
jramaswami
"""


import collections


class Solution:

    def maxOperations(self, nums, k):
        soln = 0
        freqs = collections.Counter(nums)
        for n in freqs:
            d = k - n
            print(n, d)
            if d > n:
                soln += min(freqs[n], freqs[d])
            elif d == n:
                soln += (freqs[n] // 2)
        return soln


def test_1():
    nums = [1,2,3,4]
    k = 5
    expected = 2
    assert Solution().maxOperations(nums, k) == expected


def test_2():
    nums = [3,1,3,4,3]
    k = 6
    expected = 1
    assert Solution().maxOperations(nums, k) == expected
