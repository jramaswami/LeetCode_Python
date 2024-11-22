"""
LeetCode
1072. Flip Columns For Maximum Number of Equal Rows
November 2024 Challenge
jramaswami

Thank You Neetcode.IO!
"""


import collections


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        def to_key(row):
            if row[0] == 0:
                return ''.join(str(x) for x in row)
            return ''.join('0' if x else '1' for x in row)
        
        freqs = collections.Counter(to_key(r) for r in matrix)
        return max(freqs.values())
