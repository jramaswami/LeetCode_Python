"""
LeetCode :: Arithmetic Slices II - Subsequences
November 2022 Challenge
jramaswami
"""


import collections


class Solution:

    def numberOfArithmeticSlices(self, nums):
        N = len(nums)

        # Dynamic programming.
        # dp[index][delta][length] = frequency
        dp = [collections.defaultdict(lambda: collections.defaultdict(int)) for _ in nums]
        for j, right in enumerate(nums[1:], start=1):
            for i, left in enumerate(nums[:j]):
                delta = right - left
                # Make sequence of 2 numbers.
                dp[j][delta][2] += 1
                for length, k in dp[i][delta].items():
                    dp[j][delta][length+1] += k

        # Count solutions.
        soln = 0
        for i, _ in enumerate(nums):
            for delta in dp[i]:
                for length, freq in dp[i][delta].items():
                    if length >= 3:
                        soln += freq
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