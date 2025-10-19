"""
LeetCode
1625. Lexicographically Smallest String After Applying Operations
October 2025 Challenge
jramaswami
"""


import collections


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add(t):
            u = []
            for i, c in enumerate(t):
                if i % 2 == 1:
                    x = int(c) + a
                    u.append(x % 10)
                else:
                    u.append(c)
            return ''.join(str(n) for n in u)

        soln = ''.join('9' for _ in s)
        visited = set()
        visited.add(s)
        queue = collections.deque()
        queue.append(s)
        while queue:
            t = queue.popleft()
            soln = min(soln, t)
            u = t[-b:] + t[:-b]
            if u not in visited:
                visited.add(u)
                queue.append(u)
            v = add(t)
            if v not in visited:
                visited.add(v)
                queue.append(v)
        return soln