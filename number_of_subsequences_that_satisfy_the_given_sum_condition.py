"""
LeetCode
1498. Number of Subsequences That Satisfy the Given Sum Condition
June 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = pow(10,9)+7
        nums.sort()
        soln = 0
        j = 0
        for i, min_num in enumerate(nums):
            if min_num * 2 > target:
                break
            while j+1 < len(nums) and min_num + nums[j+1] <= target:
                j += 1
            while j >= 0 and min_num + nums[j] > target:
                j -= 1
            soln += pow(2, j-i, MOD)
            soln %= MOD
        return soln % MOD


def test_1():
    nums = [3,5,6,7]
    target = 9
    expected = 4
    assert Solution().numSubseq(nums, target) == expected


def test_2():
    nums = [3,3,6,8]
    target = 10
    expected = 6
    assert Solution().numSubseq(nums, target) == expected


def test_3():
    nums = [2,3,3,4,6,7]
    target = 12
    expected = 61
    assert Solution().numSubseq(nums, target) == expected