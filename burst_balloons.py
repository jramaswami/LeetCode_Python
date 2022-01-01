"""
LeetCode :: January 2022 Challenge :: 312. Burst Balloons
jramaswami


Thank You Larry!
"""


class Solution:
    def maxCoins(self, nums):

        nums = [1] + nums + [1]
        # DP array holds State for given subarray.
        dp = [[0 for _ in nums] for _ in nums]

        # Dynamic programming to find solution.
        for length in range(1, len(nums)+1):
            for left in range(len(nums) - length + 1):
                right = left + length - 1
                for last in range(left+1, right):
                    dp[left][right] = max(
                            dp[left][right],
                            dp[left][last] + dp[last][right] + (nums[left] * nums[last] * nums[right])
                    )
        return dp[0][-1]


def test_1():
    nums = [3,1,5,8]
    assert Solution().maxCoins(nums) == 167


def test_2():
    nums = [1,5]
    assert Solution().maxCoins(nums) == 10


def test_3():
    nums = [100] * 500
    assert Solution().maxCoins(nums) == 498010100
