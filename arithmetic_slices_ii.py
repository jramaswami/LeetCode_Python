"""
LeetCode :: Arithmetic Slices II - Subsequences
November 2022 Challenge
jramaswami
"""


import collections


class Solution:

    def numberOfArithmeticSlices(self, nums):
        N = len(nums)
        soln = 0
        # dp[index][length of arithmetic sequence][delta] = frequency
        dp = [[collections.defaultdict(int) for _ in range(N+1)] for _ in nums]
        for j, right in enumerate(nums[1:], start=1):
            for i, left in enumerate(nums[:j]):
                k = right - left
                # At minimum create sequence of length 2.
                dp[j][2][k] = 1
                for length in range(2, N):
                    # Extend each sequence by 1.
                    dp[j][length+1][k] += dp[i][length][k]
                    soln += dp[j][length + 1][k]
        return soln


def test_1():
    nums = [2,4,6,8,10]
    assert Solution().numberOfArithmeticSlices(nums) == 7


def test_2():
    nums = [7,7,7,7,7]
    assert Solution().numberOfArithmeticSlices(nums) == 16


def test_3():
    nums = [2,2,3,4]
    assert Solution().numberOfArithmeticSlices(nums) == 2