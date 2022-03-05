"""
LeetCode :: March 2022 Challenge :: 740. Delete and Earn
jramaswami
"""


import collections
import functools


class Solution:

    def deleteAndEarn(self, nums):

        freqs = collections.Counter(nums)
        MAX_N = max(nums)

        @functools.cache
        def solve(n):
            if n > MAX_N:
                return 0

            return max(
                (n * freqs[n]) + solve(n+2),
                solve(n+1)
            )

        return solve(0)


def test_1():
    nums = [3,4,2]
    expected = 6
    assert Solution().deleteAndEarn(nums)


def test_2():
    nums = [2,2,3,3,3,4]
    expected = 9
    assert Solution().deleteAndEarn(nums)
