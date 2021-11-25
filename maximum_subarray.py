"""
LeetCode :: November 2021 Challenge :: 53. Maximum Subarray
jramaswami
"""


class Solution:

    def maxSubArray(self, nums):
        # Kadane's algorithm
        curr_sum = 0
        max_sum = 0
        for n in nums:
            curr_sum = max(0, curr_sum + n)
            max_sum = max(max_sum, curr_sum)
        return max_sum


def test_1():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    expected = 6
    assert Solution().maxSubArray(nums) == expected


def test_2():
    nums = [1]
    expected = 1
    assert Solution().maxSubArray(nums) == expected


def test_3():
    nums = [-1]
    expected = -1
    assert Solution().maxSubArray(nums) == expected
