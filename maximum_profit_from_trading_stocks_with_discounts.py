"""
LeetCode
3562. Maximum Profit from Trading Stocks with Discounts
December 2025 Challenge
jramaswami

REF: https://leetcode.doocs.org/en/lc/3562/
"""


import collections
from typing import List


class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        # Build a graph
        graph = collections.defaultdict(list)
        for u, v in hierarchy:
            graph[u].append(v)

        def dfs(curr):
            children_maximum_subtree_profit = [[0, 0] for _ in range(budget+1)]
            for child in graph[curr]:
                child_maximum_subtree_profit = dfs(child)
                for j in range(budget, -1, -1):
                    for jv in range(j+1):
                        for boss_bought in (0, 1):
                            val = (
                                children_maximum_subtree_profit[j- jv][boss_bought] +
                                child_maximum_subtree_profit[jv][boss_bought]
                            )
                            if val > children_maximum_subtree_profit[j][boss_bought]:
                                children_maximum_subtree_profit[j][boss_bought] = val

            maximum_subtree_profit = [[0, 0] for _ in range(budget+1)]
            price = future[curr-1]
            for j in range(budget+1):
                for boss_bought in (0, 1):
                    cost = present[curr-1] // (boss_bought + 1)
                    if j >= cost:
                        maximum_subtree_profit[j][boss_bought] = max(
                            children_maximum_subtree_profit[j][0],
                            children_maximum_subtree_profit[j-cost][1] + (price - cost)
                        )
                    else:
                        maximum_subtree_profit[j][boss_bought] = children_maximum_subtree_profit[j][0]
            return maximum_subtree_profit

        return dfs(1)[budget][0]



def test_1():
    n = 2
    present = [1,2]
    future = [4,3]
    hierarchy = [[1,2]]
    budget = 3
    expected = 5
    assert Solution().maxProfit(n, present, future, hierarchy, budget) == expected


def test_2():
    n = 2
    present = [3,4]
    future = [5,8]
    hierarchy = [[1,2]]
    budget = 4
    expected = 4
    assert Solution().maxProfit(n, present, future, hierarchy, budget) == expected


def test_3():
    n = 3
    present = [4,6,8]
    future = [7,9,11]
    hierarchy = [[1,2],[1,3]]
    budget = 10
    expected = 10
    assert Solution().maxProfit(n, present, future, hierarchy, budget) == expected