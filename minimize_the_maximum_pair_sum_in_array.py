"""
LeetCode
1877. Minimize Maximum Pair Sum in Array
November 2023 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        t = collections.deque(sorted(nums))
        soln = 0
        while t:
            soln = max(t[0]+t[-1], soln)
            t.popleft()
            t.pop()
        return soln


def test_1():
    nums = [3,5,2,3]
    expected = 7
    assert Solution().minPairSum(nums) == expected


def test_2():
    nums = [3,5,4,2,4,6]
    expected = 8
    assert Solution().minPairSum(nums) == expected