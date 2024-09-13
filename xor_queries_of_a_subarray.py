"""
LeetCode
1310. XOR Queries of a Subarray
September 2024 Challenge
jramaswami
"""


import itertools
import operator


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = list(itertools.accumulate(arr, operator.xor))

        def get(i, j):
            if i - 1 < 0:
                return prefix[j]
            return prefix[j] ^ prefix[i-1]

        return [get(i, j) for i, j in queries]
