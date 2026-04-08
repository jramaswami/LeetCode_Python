"""
LeetCode
3653. XOR After Range Multiplication Queries I
April 2026 Challenge
jramaswami
"""


from typing import List
import functools
import operator


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:

        MOD = pow(10, 9) + 7
        def query(left, right, k, v):
            i = left
            while i <= right:
                nums[i] = (nums[i] * v)
                nums[i] %= MOD
                i += k

        for q in queries:
            query(*q)
        return functools.reduce(operator.xor, nums)