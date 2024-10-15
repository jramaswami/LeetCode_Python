"""
LeetCode
2938. Separate Black and White Balls
October 2024 Challenge
jramaswami
"""


class Solution:
    def minimumSteps(self, s: str) -> int:
        soln = 0
        curr = 0
        for c in s:
            if c == '1':
                curr += 1
            if c == '0':
                soln += curr
        return soln