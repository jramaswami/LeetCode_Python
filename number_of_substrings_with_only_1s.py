"""
LeetCode
1513. Number of Substrings With Only 1s
November 2025 Challenge
jramaswami
"""


class Solution:
    def numSub(self, s: str) -> int:
        MOD = pow(10, 9) + 7
        curr_length = 0
        soln = 0
        for char in s:
            if char == '0':
                curr_length = 0
            else:
                curr_length += 1
                curr_length %= MOD
                soln += curr_length
                soln %= MOD
        return soln % MOD