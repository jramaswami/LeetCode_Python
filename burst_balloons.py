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
        dp = [[None for _ in nums] for _ in nums]

        # Helper functions.
        def get_coins(index):
            "Return the number of coins you get for a given index."
            if index < 0 or index >= len(nums):
                return 1
            return nums[index]

        def get_burst_coins(left, right):
            "Return the number of coinds you get for bursting subarray."
            if left > right:
                return 0
            if dp[left][right] is None:
                return 0
            return dp[left][right].coins

        # Dynamic programming to find solution.
        for length in range(1, len(nums)+1):
            for left in range(len(nums) - length + 1):
                right = left + length - 1
                # Consider subarray [left:right+1], find the best balloon to
                # burst last.
                best_coins = 0
                best_balloon = 0
                for last in range(left, right+1):
                    # Consider last balloon to burst at given index.
                    # Get the best from the left part of the subarray.
                    left_coins = get_burst_coins(left, last-1)
                    # Get the best from the right part of the subarray.
                    right_coins = get_burst_coins(last+1, right)
                    # Now get the coins from bursting last balloon, which will
                    # be grouped with the balloons adjacent but outside the
                    # subarray because we have already burst all the other
                    # balloons in the subarray.
                    last_coins = get_coins(left - 1) * get_coins(last) * get_coins(right + 1)
                    total_coins = left_coins + last_coins + right_coins
                    if total_coins > best_coins:
                        best_coins, best_balloon = total_coins, last
                # Record the best State in the dp array.
                dp[left][right] = State(best_coins, best_balloon)

        return dp[0][-1].coins


def test_1():
    nums = [3,1,5,8]
    assert Solution().maxCoins(nums) == 167


def test_2():
    nums = [1,5]
    assert Solution().maxCoins(nums) == 10


def test_3():
    nums = [100] * 500
    assert Solution().maxCoins(nums) == 498010100
