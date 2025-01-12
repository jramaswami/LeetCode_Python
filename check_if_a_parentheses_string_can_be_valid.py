"""
LeetCode
2116. Check if a Parentheses String Can Be Valid
January 2025 Challenge
jramaswami

Thank You NeetCode.IO!
"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        locked_stack = []
        unlocked_stack = []

        for i, (char, lock) in enumerate(zip(s, locked)):
            if lock == '0':
                unlocked_stack.append(i)
            elif s[i] == '(':
                locked_stack.append(i)
            else:  # ')'
                if locked_stack:
                    locked_stack.pop()
                elif unlocked_stack:
                    unlocked_stack.pop()
                else:
                    return False
        
        while locked_stack:
            if locked_stack[-1] > unlocked_stack[-1]:
                return False
            locked_stack.pop()
            unlocked_stack.pop()

        return len(unlocked_stack) % 2 == 0
