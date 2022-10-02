"""
LeetCode :: October 2022 Challenge :: 1155. Number of Dice Rolls With Target Sum
jramaswami
"""


class Solution:

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = pow(10, 9) + 7
        prev_dp = [0 for _ in range(target+1)]
        prev_dp[0] = 1   # There is one way to get 0 with 0 dice.
        curr_dp = [0 for _ in range(target+1)]
        for _ in range(n):
            for t in range(target+1):
                if prev_dp[t] > 0:
                    for x in range(1,k+1):
                        if t + x > target:
                            break
                        curr_dp[t+x] += prev_dp[t]
                        curr_dp[t+x] %= MOD
            prev_dp, curr_dp = curr_dp, [0 for _ in range(target+1)]
        return prev_dp[target] % MOD


def test_1():
    n = 1
    k = 6
    target = 3
    expected = 1
    assert Solution().numRollsToTarget(n, k, target) == expected


def test_2():
    n = 2
    k = 6
    target = 7
    expected = 6
    assert Solution().numRollsToTarget(n, k, target) == expected


def test_3():
    n = 30
    k = 30
    target = 500
    expected = 222616187
    assert Solution().numRollsToTarget(n, k, target) == expected