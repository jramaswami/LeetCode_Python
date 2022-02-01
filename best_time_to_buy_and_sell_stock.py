"""
LeetCode :: February 2022 Challenge :: 121. Best Time to Buy and Sell Stock
jramaswami
"""


from math import inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = inf
        max_sell = 0
        soln = 0
        for sell in prices:
            min_buy = min(min_buy, sell)
            soln = max(soln, sell - min_buy)
        return soln
