"""
LeetCode
955. Delete Columns to Make Sorted II
December 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def columns_are_sorted(i):
            return all(a[i] <= b[i] for a, b in zip(strs[:-1], strs[1:]))

        soln = 0
        for i, _ in enumerate(strs[0]):
            if columns_are_sorted(i):
                break
            soln += 1
        return soln