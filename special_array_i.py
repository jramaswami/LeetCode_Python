"""
LeetCode
3151. Special Array I
February 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i, _ in enumerate(nums[:-1]):
            if (nums[i] % 2) == (nums[i+1] % 2):
                return False
        return True
