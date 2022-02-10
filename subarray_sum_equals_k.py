"""
LeetCode :: February 2022 Challenge :: 560. Subarray Sum Equals K
jramaswami
"""


import collections


class Solution:
    def subarraySum(self, nums, k):
        # k = curr_sum - prev_sum
        # k + prev_sum = curr_sum
        # prev_sum = curr_sum - k
        soln = 0
        curr_sum = 0
        prev_sums = collections.Counter()
        prev_sums[0] = 1
        for n in nums:
            curr_sum += n
            delta = curr_sum - k
            soln += prev_sums[delta]
            prev_sums[curr_sum] += 1
        return soln


def test_1():
    nums = [1,1,1]
    k = 2
    expected = 2
    assert Solution().subarraySum(nums, k) == 2


def test_2():
    nums = [1,2,3]
    k = 3
    expected = 2
    assert Solution().subarraySum(nums, k) == 2
