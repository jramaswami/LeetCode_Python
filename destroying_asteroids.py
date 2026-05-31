"""
LeetCode
2126. Destroying Asteroids
May 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if a > mass:
                return False
            mass += a
        return True