"""
LeetCode
2696. Minimum String Length After Removing Substrings
October 2024 Challenge
jramaswami
"""


class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for c in s:
            stack.append(c)
            while len(stack) >= 2 and stack[-2:] in (['A', 'B'], ['C', 'D']):
                stack.pop()
                stack.pop()
        return len(stack)
