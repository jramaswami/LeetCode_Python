"""
LeetCode
2411. Smallest Subarrays With Maximum Bitwise OR
July 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # Compute an OR suffix array with the max or for B[i:j]
        suffix = [0 for _ in nums]
        curr = 0
        for i in range(len(nums)-1, -1, -1):
            curr |= nums[i]
            suffix[i] = curr
        # Brute force
        soln = []
        for i, _ in enumerate(nums):
            max_or = suffix[i]
            curr = 0
            for j, n in enumerate(nums[i:], start = i):
                curr |= n
                if curr == max_or:
                    soln.append(j - i + 1)
                    break
        return soln