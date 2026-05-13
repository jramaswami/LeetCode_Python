"""
LeetCode
1674. Minimum Moves to Make Array Complementary
May 2026 Challenge
jramaswami

REF: https://algo.monster/liteproblems/1674
"""


from typing import List
import itertools


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        differences = [0 for _ in range(2 * limit + 2)]
        for i in range(len(nums) // 2):
            left = nums[i]
            right = nums[len(nums) - i - 1]
            if left > right:
                left, right = right, left
            differences[2] += 2
            differences[left + 1] -= 2
            differences[left + 1] += 1
            differences[left + right] -= 1
            differences[left + right + 1] += 1
            differences[right + limit + 1] -= 1
            differences[right + limit + 1] += 2
        return min(itertools.accumulate(differences[2:]))