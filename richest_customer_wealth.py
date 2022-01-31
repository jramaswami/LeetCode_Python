"""
LeetCode :: January 2022 Challenge :: 1672. Richest Customer Wealth
jramaswami
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(t) for t in accounts)
