"""
LeetCode
1475. Final Prices With a Special Discount in a Shop
December 2024 Challenge
jramaswami
"""


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discounts = [0 for _ in prices]
        for i, p in enumerate(prices):
            for j, d in enumerate(prices[i+1:], start=i+1):
                if prices[j] <= prices[i]:
                    discounts[i] = prices[j]
                    break
        return [p - d for p, d in zip(prices,discounts)]
