"""
LeetCode
1569. Number of Ways to Reorder Array to Get Same BST
June 2023 Challenge
jramaswami

Thank You, Larry!
"""


from typing import *


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = pow(10, 9) + 7
        factorials = [1]
        while len(factorials) < 2 * len(nums):
            factorials.append(len(factorials) * factorials[-1])


        def c(left, right):
            return (
                factorials[len(left)+len(right)] //
                factorials[len(left)] //
                factorials[len(right)]
            ) % MOD

        def go(arr):
            if len(arr) == 0:
                return 1
            if len(arr) == 1:
                return 1

            x = arr[0]
            left = [y for y in arr if y < x]
            right = [y for y in arr if y > x]

            return (go(left) % MOD) * (go(right) % MOD) * (c(left, right) %MOD)

        return (go(nums) - 1) % MOD


def test_1():
    nums = [2,1,3]
    expected = 1
    assert Solution().numOfWays(nums) == expected


def test_2():
    nums = [3,4,5,1,2]
    expected = 5
    assert Solution().numOfWays(nums) == expected


def test_3():
    nums = [1,2,3]
    expected = 0
    assert Solution().numOfWays(nums) == expected
