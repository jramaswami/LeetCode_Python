"""
LeetCode
955. Delete Columns to Make Sorted II
December 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/955
"""


from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Corner cases
        if len(strs) <= 1:
            return 0

        deleted_columns = 0
        sorted_pairs = [False for _ in strs]
        for col, _ in enumerate(strs[0]):
            should_delete = False
            for row, _ in enumerate(strs[:-1]):
                if not sorted_pairs[row] and strs[row][col] > strs[row+1][col]:
                    deleted_columns += 1
                    should_delete = True
                    break

            if should_delete:
                continue

            for row, _ in enumerate(strs[:-1]):
                if strs[row][col] < strs[row+1][col]:
                    sorted_pairs[row] = True

        return deleted_columns