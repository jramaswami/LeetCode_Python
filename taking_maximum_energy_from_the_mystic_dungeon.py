"""
LeetCode
3147. Taking Maximum Energy From the Mystic Dungeon
October 2025 Challenge
jramaswami
"""


import itertools
from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        return max(
            max(
                itertools.accumulate(
                    itertools.islice(reversed(energy), start, len(energy), k)
                )
            )
            for start in range(k)
        )