"""
LeetCode :: March 2022 Challenge :: The K Weakest Rows in a Matrix
jramaswami
"""


class Solution:
    def kWeakestRows(self, matrix, k):
        return [t[1] for t in sorted(((sum(row), i) for i, row in enumerate(matrix)))[:k]]
