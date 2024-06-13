"""
LeetCode
2037. Minimum Number of Moves to Seat Everyone
June 2024 Challenge
jramaswami
"""


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(a-b) for a, b in zip(sorted(seats), sorted(students)))
