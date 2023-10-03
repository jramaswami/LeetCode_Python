"""
LeetCode
1512. Number of Good Pairs
October 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # There are faster ways, but n is small
        soln = 0
        for i, a in enumerate(nums):
            for b in nums[i+1:]:
                if a == b:
                    soln += 1
        return soln


def test_1():
    nums = [1,2,3,1,1,3]
    expected = 4
    assert Solution().numIdenticalPairs(nums) == expected


def test_2():
    nums = [1,1,1,1]
    expected = 6
    assert Solution().numIdenticalPairs(nums) == expected


def test_3():
    nums = [1,2,3,]
    expected = 0
    assert Solution().numIdenticalPairs(nums) == expected