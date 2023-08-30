"""
LeetCode
2366. Minimum Replacements to Sort the Array
August 2023 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=c7NZJRt89dc
"""


from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        soln = 0
        upper_bound = nums[-1]
        for n in reversed(nums[:-1]):
            operations = (n + upper_bound - 1) // upper_bound
            soln += operations - 1
            upper_bound = n // operations
        return soln


def test_1():
    nums = [3,9,3]
    expected = 2
    assert Solution().minimumReplacement(nums) == expected


def test_2():
    nums = [1,2,3,4,5]
    expected = 0
    assert Solution().minimumReplacement(nums) == expected