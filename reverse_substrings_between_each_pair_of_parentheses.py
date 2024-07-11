"""
LeetCode
1190. Reverse Substrings Between Each Pair of Parentheses
July 2024 Challenge
jramaswami
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Find matching parentheses
        matching_parens = []
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                matching_parens.append((j+1, i-1))
        
        t = list(s)
        for i, j in matching_parens:
            while i < j:
                t[i], t[j] = t[j], t[i]
                i += 1
                j -= 1
        return ''.join(c for c in t if c not in ('(', ')'))
