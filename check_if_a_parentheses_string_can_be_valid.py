"""
LeetCode
2116. Check if a Parentheses String Can Be Valid
January 2025 Challenge
jramaswami
"""


import functools


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        @functools.cache
        def rec(number_of_opens, i):
            if number_of_opens < 0:
                return False
            if i >= len(s):
                return number_of_opens == 0
            if locked[i] == '0':
                return (
                    rec(number_of_opens + 1, i + 1) or
                    rec(number_of_opens - 1, i + 1)
                )
            else:
                if s[i] == '(':
                    return rec(number_of_opens + 1, i + 1)
                else:
                    return rec(number_of_opens - 1, i + 1)
    
        return rec(0, 0)

