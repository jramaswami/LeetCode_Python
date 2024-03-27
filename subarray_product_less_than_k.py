"""
LeetCode
713. Subarray Product Less Than K
March 2024 Challenge
jramaswami
"""


from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        soln = 0
        i = 0
        p = 1
        for j, n in enumerate(nums):
            # Add n to window
            p *= n
            # Remove from left window while p >= k
            while p >= k:
                p //= nums[i]
                i += 1
            # Invariant product of nums[i:j+1] < k
            soln += j + 1 - i
        return soln


def test_1():
    nums = [10, 5, 2, 6]
    k = 100
    expected = 8
    assert Solution().numSubarrayProductLessThanK(nums, k) == expected


def test_2():
    nums = [1, 2, 3]
    k = 0
    expected = 0
    assert Solution().numSubarrayProductLessThanK(nums, k) == expected