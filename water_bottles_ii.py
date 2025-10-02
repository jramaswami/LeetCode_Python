"""
LeetCode
3100. Water Bottles II
October 2025 Challenge
jramaswami
"""


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = 0
        bottlesDrank = 0
        while numBottles or (emptyBottles >= numExchange):
            if emptyBottles >= numExchange:
                emptyBottles -= numExchange
                numBottles += 1
                numExchange += 1
            else:
                emptyBottles += numBottles
                bottlesDrank += numBottles
                numBottles = 0
        return bottlesDrank