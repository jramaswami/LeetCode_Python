"""
LeetCode
1925. Count Square Sum Triples
December 2025 Challenge
jramaswami
"""


class Solution:
    def countTriples(self, n: int) -> int:
        squares = set()
        squares = {x * x for x in range(1, n+1)}
        n_squared = n * n
        soln = 0
        for a in range(1, n):
            for b in range(1, n):
                c_squared = (a * a) + (b * b)
                if c_squared > n_squared:
                    break
                if c_squared in squares:
                    soln += 1
        return soln