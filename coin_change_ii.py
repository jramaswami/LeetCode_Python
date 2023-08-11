"""
LeetCode
518. Coin Change II
August 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[coin_index+1][amount] = number of ways to reach
        prev_dp = [0 for _ in range(amount+1)]
        curr_dp = [0 for _ in range(amount+1)]
        prev_dp[0] = 1
        for c in coins:
            for a, _ in enumerate(curr_dp):
                curr_dp[a] += prev_dp[a]
                if a + c <= amount:
                    curr_dp[a + c] += curr_dp[a]
            prev_dp, curr_dp = curr_dp, [0 for _ in range(amount+1)]
        return prev_dp[-1]


def test_1():
    amount = 5
    coins = [1,2,5]
    expected = 4
    assert Solution().change(amount, coins) == expected


def test_2():
    amount = 3
    coins = [2]
    expected = 0
    assert Solution().change(amount, coins) == expected


def test_3():
    amount = 10
    coins = [10]
    expected = 1
    assert Solution().change(amount, coins) == expected



