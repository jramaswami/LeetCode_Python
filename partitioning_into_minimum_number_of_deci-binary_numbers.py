"""
LeetCode
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
March 2026 Challenge
jramaswami
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(c) for c in n)
