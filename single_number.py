"""
LeetCode :: Single Number
jramaswami
"""
from functools import reduce
from operator import xor
from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums, 0)

