"""
LeetCode
2946. Matrix Similarity After Cyclic Shifts
March 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k = k % len(mat[0])
        odd_offset = k
        even_offset = (len(mat[0]) - k) % len(mat[0])
        for r, row in enumerate(mat):
            for c, _ in enumerate(row):
                if c % 2:
                    c0 = (c + odd_offset) % len(row)
                else:
                    c0 = (c + even_offset) % len(row)
                if row[c] != row[c0]:
                    return False
        return True