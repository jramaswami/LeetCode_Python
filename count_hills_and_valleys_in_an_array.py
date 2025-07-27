"""
LeetCode
2210. Count Hills and Valleys in an Array
July 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Remove adjacent duplicate values
        nums0 = []
        for n in nums:
            if not nums0:
                nums0.append(n)
            elif nums0[-1] != n:
                nums0.append(n)

        # Count hills and valleys
        count = 0
        for i in range(1, len(nums0)-1):
            a, b, c = nums0[i-1:i+2]
            if a < b and c < b:
                count += 1
            elif a > b and c > b:
                count += 1
        return count