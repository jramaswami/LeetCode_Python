"""
LeetCode
3652. Best Time to Buy and Sell Stock using Strategy
December 2025 Challenge
jramaswami
"""


import itertools
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        prices_prefix = list(accumulate(prices))
        delta = [s * p for s, p in zip(strategy, prices)]
        delta_prefix = list(accumulate(delta))
        delta_suffix = list(accumulate(reversed(delta)))[::-1]

        def get(a, left, right):
            if left == 0:
                return a[right]
            return a[right] - a[left-1]

        soln = delta_prefix[-1]
        for i, _ in enumerate(prices):
            if i + k > len(prices):
                break
            left = get(delta_prefix, 0, i - 1) if i else 0
            right = delta_suffix[i + k] if i + k < len(prices) else 0
            middle = get(prices_prefix, i + (k // 2), i + k - 1)
            j = i + k
            soln = max(soln, left + middle + right)
        return soln