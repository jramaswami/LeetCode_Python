"""
LeetCode
787. Cheapest Flights Within K Stops
January 2023 Challenge
jramaswami
"""


import math
from typing import *


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [math.inf for _ in range(n)]
        cost[src] = 0
        new_cost = [math.inf for _ in range(n)]
        for _ in range(k+1):
            for u, v, c in flights:
                new_cost[v] = min(new_cost[v], cost[u] + c)
            cost, new_cost = new_cost, [math.inf for _ in range(n)]
        return (cost[dst] if cost[dst] < math.inf else -1)


def test_1():
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    expected = 700
    assert Solution().findCheapestPrice(n, flights, src, dst, k) == expected


def test_2():
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    expected = 200
    assert Solution().findCheapestPrice(n, flights, src, dst, k) == expected


def test_3():
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    expected = 500
    assert Solution().findCheapestPrice(n, flights, src, dst, k) == expected


def test_4():
    "WA"
    n = 4
    flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    k = 1
    expected = 6
    assert Solution().findCheapestPrice(n, flights, src, dst, k) == expected


def test_5():
    "WA"
    n = 3
    flights = [[0,1,2],[1,2,1],[2,0,10]]
    src = 1
    dst = 2
    k = 1
    expected = 1
    assert Solution().findCheapestPrice(n, flights, src, dst, k) == expected