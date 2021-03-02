"""
LeetCode :: March 2021 Challenge :: Set Mismatch
jramaswami
"""
from typing import *


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        frequency = [0 for _ in range(N+1)]
        for n in nums:
            frequency[n] += 1

        duplicate = 0
        missing = 0
        for n in range(1, N+1):
            if frequency[n] == 2:
                duplicate = n
            elif frequency[n] == 0:
                missing = n
        return [duplicate, missing]


def test_1():
    assert Solution().findErrorNums([1, 2, 2, 4]) == [2, 3]

def test_2():
    assert Solution().findErrorNums([1, 1]) == [1, 2]
