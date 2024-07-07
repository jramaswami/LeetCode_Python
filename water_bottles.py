"""
LeetCode
1518. Watter Bottles
July 2024 Challenge
jramaswami
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        soln = carry = 0
        while numBottles > 0:
            soln += numBottles
            numBottles, carry = divmod(numBottles + carry, numExchange)
        return soln
