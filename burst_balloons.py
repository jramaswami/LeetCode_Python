"""
LeetCode :: January 2022 Challenge :: 312. Burst Balloons
jramaswami


REF: https://www.youtube.com/watch?v=IFNibRVgFBo
"""


import collections


State = collections.namedtuple('State', ['coins', 'last'])


class Solution:
    def maxCoins(self, nums):

        # DP array holds State for given subarray.
        dp = [[0 for _ in nums] for _ in nums]

        # Dynamic programming to find solution.
        for length in range(1, len(nums)+1):
            for left in range(len(nums) - length + 1):
                right = left + length - 1
                # Consider subarray [left:right+1], find the best balloon to
                # burst last.

                # Get the values of the two coins to the far left and far
                # right (the coins just outside the subarray).
                far_left = nums[left - 1] if 0 <= left - 1 else 1
                far_right = nums[right + 1] if right + 1 < len(nums) else 1

                for last in range(left, right+1):
                    # Consider last balloon to burst at given index.
                    # Get the best from the left part of the subarray.
                    left_coins = left_coins = dp[left][last-1] if left <= last - 1 else 0
                    # Get the best from the right part of the subarray.
                    right_coins = right_coins = dp[last+1][right] if last + 1 <= right else 0
                    # Now get the coins from bursting last balloon, which will
                    # be grouped with the balloons adjacent but outside the
                    # subarray because we have already burst all the other
                    # balloons in the subarray.
                    last_coins = far_left * nums[last] * far_right
                    total_coins = left_coins + last_coins + right_coins
                    # Record the best number of coins in the dp array.
                    dp[left][right] = max(dp[left][right], total_coins)

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
