"""
LeetCode
921. Minimum Add to Make Parentheses Valid
October 2024 Challenge
jramaswami
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openers = 0
        soln = 0
        for c in s:
            if c == '(':
                openers += 1
            elif c == ')':
                if openers > 0:
                    openers -= 1
                else:
                    soln += 1
        return soln + openers
