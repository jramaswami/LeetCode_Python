"""
LeetCode
2109. Adding Spaces to a String
December 2024 Challenge
jramaswami
"""


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i = 0
        stack = []
        for j, c in enumerate(s):
            if i < len(spaces) and spaces[i] == j:
                stack.append(' ')
                stack.append(c)
                i += 1
            else:
                stack.append(c)
        return ''.join(stack)
