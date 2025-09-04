"""
LeetCode
3516. Find Closest Person
September 2025 Challenge
jramaswami
"""


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx = abs(x - z)
        dy = abs(y - z)
        if dx < dy:
            return 1
        elif dx > dy:
            return 2
        return 0