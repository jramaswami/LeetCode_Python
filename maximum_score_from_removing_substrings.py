"""
LeetCode
1717. Maximum Score From Removing Substrings
July 2024 Challenge
jramaswami
"""


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(code, t):
            """Remove the two letter code from t.
            Return the number of removals and the remaining letters
            """
            stack = []
            removals = 0
            a, b = code
            for c in t:
                if c == b and stack and stack[-1] == a:
                    stack.pop()
                    removals += 1
                else:
                    stack.append(c)
            return removals, stack

        soln = 0
        n, t = remove('ab', s)
        m, t = remove('ba', t)
        soln = max(soln, n*x + m*y)
        n, t = remove('ba', s)
        m, _ = remove('ab', t)
        soln = max(soln, n*y + m*x)
        return soln
