"""
LeetCode
3461. Check If Digits Are Equal in String After Operations I
October 2025 Challenge
jramaswami
"""


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        curr = [int(d) for d in s]
        prev = []
        while len(curr) > 2:
            for i, _ in enumerate(curr[:-1]):
                a = curr[i]
                b = curr[i+1]
                x = (a + b) % 10
                prev.append(x)
            curr = prev
            prev = []
        return curr[0] == curr[-1]
