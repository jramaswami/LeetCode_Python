"""
LeetCode
2009. Minimum Number of Operations to Make Array Continuous
October 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Remove duplicates and sort list.
        nums0 = list(sorted(set(nums)))
        soln = len(nums) - 1
        limit = len(nums) - 1
        right = 0
        for left, _ in enumerate(nums0):
            while right < len(nums0) and nums0[right] - nums0[left] <= limit:
                right += 1
            soln = min(soln, len(nums) - (right - left))
        return soln


def test_1():
    nums = [4,2,5,3]
    expected = 0
    assert Solution().minOperations(nums) == expected


def test_2():
    nums = [1, 2, 3, 5, 6]
    expected = 1
    assert Solution().minOperations(nums) == expected


def test_3():
    nums = [1, 10, 100, 1000]
    expected = 3
    assert Solution().minOperations(nums) == expected


def test_4():
    "WA: there are duplicate numbers."
    nums = [8, 5, 9, 9, 8, 4]
    expected = 2
    assert Solution().minOperations(nums) == expected
