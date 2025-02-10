"""
LeetCode
3174. Clear Digits
February 2025 Challenge
jramaswami
"""


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for x in s:
            if x.isdigit():
                stack.pop()
            else:
                stack.append(x)
        return ''.join(stack)
