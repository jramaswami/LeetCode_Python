"""
LeetCode :: May 2022 Challenge :: 191. Number of 1 Bits
jramaswami
"""


class Solution:
    def hammingWeight(self, n):
        soln = 0
        for i in range(33):
            mask = 1 << i
            if mask & n:
                soln += 1
        return soln
