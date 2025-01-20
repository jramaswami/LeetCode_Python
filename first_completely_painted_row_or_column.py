"""
LeetCode
2661. First Completely Painted Row or Column
January 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        col_painted = [0 for _ in mat[0]]
        row_painted = [0 for _ in mat]
        lookup = dict()
        for r, row in enumerate(mat):
            for c, val in enumerate(row):
                lookup[val] = (r, c)
        
        for i, x in enumerate(arr):
            r, c = lookup[x]
            col_painted[c] += 1
            row_painted[r] += 1
            if col_painted[c] == len(mat) or row_painted[r] == len(mat[0]):
                return i
