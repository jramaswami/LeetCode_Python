"""
LeetCode
3000. Maximum Area of Longest Diagonal Rectangle
August 2025 Challenge
jramaswami
"""


import math


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        longest_diagonal_squared = 0
        maximum_width = 0
        for length, width in dimensions:
            diagonal_squared = length**2 + width**2
            if diagonal_squared == longest_diagonal_squared:
                maximum_width = max(maximum_width, length * width)
                longest_diagonal_squared = diagonal_squared
            elif diagonal_squared > longest_diagonal_squared:
                maximum_width = length * width
                longest_diagonal_squared = diagonal_squared
        return maximum_width
