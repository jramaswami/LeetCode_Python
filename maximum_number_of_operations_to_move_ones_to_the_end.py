"""
LeetCode
3228. Maximum Number of Operations to Move Ones to the End
November 2025 Challenge
jramaswami
"""


class Solution:
    def maxOperations(self, s: str) -> int:
        prev = ''
        soln = 0
        ones = 0
        for char in s:
            if char == '0':
                if prev == '0':
                    pass
                else:
                    soln += ones
            else:
                ones += 1
            prev = char
        return soln