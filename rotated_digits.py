"""
LeetCode
788. Rotated Digits
May 2026 Challenge
jramaswami
"""


class Solution:
    def rotatedDigits(self, n: int) -> int:
        good = 0
        rotations = ['0', '1', '5', 'x', 'x', '2', '9', 'x', '8', '6']
        for x in range(n+1):
            a = str(x)
            b = ''.join(rotations[int(t)] for t in a)
            if 'x' not in b and a != b:
                good += 1
        return good