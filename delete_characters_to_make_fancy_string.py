"""
LeetCode
1957. Delete Characters to Make Fancy String
November 2024 Challenge
jramaswami
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) >= 2 and stack[-2] == stack[-1] and stack[-1] == c:
                continue
            else:
                stack.append(c)
        return ''.join(stack)
