"""
LeetCode
1910. Remove All Occurrences of a Substring
February 2025 Challenge
jramaswami
"""


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        def check_stack(stack, part):
            for a, b in zip(reversed(stack), reversed(part)):
                if a != b:
                    return False
            return True

        def remove_part(stack, part):
            for _ in part:
                stack.pop()
        
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= len(part) and check_stack(stack, part):
                remove_part(stack, part)
        return ''.join(stack)
