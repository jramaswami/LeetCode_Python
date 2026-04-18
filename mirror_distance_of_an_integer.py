"""
LeetCode
3783. Mirror Distance of an Integer
April 2026 Challenge
jramaswami
"""


class Solution:
    def mirrorDistance(self, n: int) -> int:
        m = int(''.join(reversed(str(n))))
        return abs(n - m)