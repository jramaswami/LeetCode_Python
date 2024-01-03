"""
LeetCode
2125. Number of Laser Beams in a Bank
January 2024 Challenge
jramaswami
"""


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers_per_row = [row.count('1') for row in bank]
        rows_with_lasers = [row for row in lasers_per_row if row > 0]
        soln = 0
        for a, b in zip(rows_with_lasers[:-1], rows_with_lasers[1:]):
            soln += a * b
        return soln