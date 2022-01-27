"""
LeetCode :: January 2022 Challenge :: 421. Maximum XOR of Two Numbers in an Array
jramaswami
"""


import itertools
import operator

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0] ^ nums[0]
        return max(operator.xor(*pair) for pair in itertools.combinations(nums, 2))
