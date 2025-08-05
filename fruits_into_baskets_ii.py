"""
LeetCode
3477. Fruits Into Baskets II
August 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        allocated = 0
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if fruit <= basket:
                    baskets[i] = 0
                    allocated += 1
                    break
        return len(fruits) - allocated