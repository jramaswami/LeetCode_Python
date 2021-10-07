"""
LeetCode :: 930. Binary Subarrays With Sum
jramaswami
"""


from collections import defaultdict


class Solution:

    def numSubarraysWithSum(self, nums, target_sum):
        prev_sums = defaultdict(int)
        prev_sums[0] += 1
        curr_sum = 0
        soln = 0
        for n in nums:
            curr_sum += n
            delta = curr_sum - target_sum
            soln += prev_sums[delta]
            prev_sums[curr_sum] += 1
        return soln


def test_1():
    nums = [1,0,1,0,1]
    goal = 2
    expected = 4
    assert Solution().numSubarraysWithSum(nums, goal) == expected


def test_2():
    nums = [0,0,0,0,0]
    goal = 0
    expected = 15
    assert Solution().numSubarraysWithSum(nums, goal) == expected
