"""
LeetCode
2138. Divide a String Into Groups of Size k
June 2025 Challenge
jramaswami
"""


import itertools


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        soln = []
        for char in s:
            if not soln or len(soln[-1]) == k:
                soln.append([])
            soln[-1].append(char)
        while len(soln[-1]) < k:
            soln[-1].append(fill)
        return [''.join(part) for part in soln]