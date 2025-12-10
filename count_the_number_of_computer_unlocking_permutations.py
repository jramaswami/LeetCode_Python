"""
LeetCode
3577. Count the Number of Computer Unlocking Permutations
December 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        m = complexity[0]
        if any(n <= m for n in complexity[1:]):
            return 0
        MOD = pow(10, 9) + 7
        soln = 1
        N = len(complexity)
        for n in range(1, N):
            soln *= n
            soln %= MOD
        return soln