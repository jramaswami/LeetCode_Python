"""
LeetCode
1975. Maximum Matrix Sum
November 2024 Challenge
jramaswami
"""


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        matrix_sum = sum(sum(abs(x) for x in row) for row in matrix)
        neg_count = sum(sum(1 if x < 0 else 0 for x in row) for row in matrix)
        if neg_count % 2:
            min_number = min(min(abs(x) for x in row) for row in matrix)
            matrix_sum -= (2 * min_number)
        return matrix_sum
