"""
LeetCode
2200. Find All K-Distant Indices in an Array
June 2025 Challenge
jramaswami
"""


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        soln = []
        for i, n in enumerate(nums):
            for j, x in enumerate(nums):
                if x == key and abs(i - j) <= k:
                    soln.append(i)
                    break
        return soln