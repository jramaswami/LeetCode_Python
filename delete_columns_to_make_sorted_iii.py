"""
LeetCode
960. Delete Columns to Make Sorted III
December 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/960
"""


from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        dp = [1 for _ in strs[0]]
        for curr_col, _ in enumerate(strs[0]):
            for prev_col, _ in enumerate(strs[0][:curr_col]):
                if all(s[prev_col] <= s[curr_col] for s in strs):
                    dp[curr_col] = max(dp[curr_col], dp[prev_col] + 1)
        return len(strs[0]) - max(dp)