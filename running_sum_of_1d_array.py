"""
Leet Code :: May 2021 Challenge :: Running Sum of 1d Array
jramaswami
"""
from itertools import accumulate


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))
