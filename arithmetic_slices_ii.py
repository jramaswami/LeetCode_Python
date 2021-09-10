"""
LeetCode :: September 2021 Challenge :: Arithmetic Slices II - Subsequences
jramaswami
"""


from collections import defaultdict


class Solution:

    def numberOfArithmeticSlices(self, nums):

        # Deltas is a dict of dict.
        # deltas[nums index][delta][length][how many ways to reach]
        deltas = [defaultdict(lambda: defaultdict(int)) for _ in nums]
        for i, (n, dn) in enumerate(zip(nums, deltas)):
            for j, (m, dm) in enumerate(zip(nums[i+1:], deltas[i+1:]), start=i+1):
                dx = m - n
                # We can start from nums[i] and nums[j]
                deltas[j][dx][2] += 1
                # For every way to reach nums[i] with the delta dx we can
                # extend the length of that subsequence to include nums[j].
                # So, we can reach nums[j] with a subsequence of length + 1
                # with a delta of dx in the same number of ways we can reach
                # nums[i] with a subsequence of length and a delta of dx.
                for length, number_of_ways in deltas[i][dx].items():
                    deltas[j][dx][length+1] += number_of_ways

        soln = 0
        for i, delta in enumerate(deltas):
            for dx in delta:
                for length, number_of_ways in delta[dx].items():
                    if length >= 3:
                        soln += number_of_ways
        return soln


def test_1():
    nums = [2,4,6,8,10]
    assert Solution().numberOfArithmeticSlices(nums) == 7


def test_2():
    nums = [7,7,7,7,7]
    assert Solution().numberOfArithmeticSlices(nums) == 16
