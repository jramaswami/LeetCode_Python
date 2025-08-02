"""
LeetCode
2561. Rearranging Fruits
August 2025 Challenge
jramaswami

REF: https://www.simplyleet.com/rearranging-fruits
"""


import collections
import itertools
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Combined frequency of all fruits
        all_fruits = collections.Counter(itertools.chain(basket1, basket2))
        # There must be an even number of fruits
        if any(freq % 2 == 1 for freq in all_fruits.values()):
            return -1

        # Frequency in each basket
        freq1 = collections.Counter(basket1)
        freq2 = collections.Counter(basket2)

        # Swaps where there is too many in a basket
        excess1 = []
        excess2 = []

        for fruit, freq in all_fruits.items():
            # There should be half the fruit in each basket
            target = freq // 2
            if freq1[fruit] > target:
                # Add a swap for each excess fruit
                excess1.extend([fruit] * (freq1[fruit] - target))
            if freq2[fruit] > target:
                # Add a swap for each excess fruit
                excess2.extend([fruit] * (freq2[fruit] - target))

        # Sort swaps so we can pair smallest in 1 with largest in 2
        excess1.sort()
        excess2.sort(reverse=True)

        # Compute total swap cost
        # When swapping fruits, we could swap directly
        # or we could swap each fruit with the smallest fruit
        # because each basket has at least 1 of the smallest fruit.
        # Two swaps would return the smallest fruit to the same
        # state and exchange the other two fruits at a cost of
        # 2 * the smallest fruit
        smallest_fruit = min(all_fruits)
        indirect_swap_cost = 2 * smallest_fruit
        total_cost = 0
        for fruit1, fruit2 in zip(excess1, excess2):
            direct_swap_cost = min(fruit1, fruit2)
            total_cost += min(direct_swap_cost, indirect_swap_cost)
        return total_cost