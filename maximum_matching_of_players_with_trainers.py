"""
LeetCode
2410. Maximum Matching of Players With Trainers
July 2025 Challenge
jramaswami
"""


import heapq
from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        heapq.heapify(trainers)
        soln = 0
        for p in players:
            while trainers and trainers[0] < p:
                heapq.heappop()
            if trainers:
                heapq.heappop()
        return soln