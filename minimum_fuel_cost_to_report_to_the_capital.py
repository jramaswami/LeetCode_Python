"""
LeetCode
2477. Minimum Fuel Cost to Report to the Capital
February 2023 Challenge
jramaswami
"""


import collections
import math
from typing import *


Result = collections.namedtuple('Result', ['reps', 'fuel'])


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # Convert to adj.
        adj = [[] for _ in range(len(roads) + 1)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)

        def traverse(node, parent):
            prev_reps = prev_fuel = 0
            for neighbor in adj[node]:
                if neighbor != parent:
                    r, f = traverse(neighbor, node)
                    prev_reps += r
                    prev_fuel += f
            curr_reps = prev_reps + 1
            curr_fuel = prev_fuel + math.ceil(curr_reps / seats)
            return curr_reps, curr_fuel

        soln = 0
        for neighbor in adj[0]:
            _, f = traverse(neighbor, 0)
            soln += f
        return soln



def test_1():
    roads = [[0,1],[0,2],[0,3]]
    seats = 5
    expected =  3
    assert Solution().minimumFuelCost(roads, seats) == expected


def test_2():
    roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
    seats = 2
    expected=  7
    assert Solution().minimumFuelCost(roads, seats) == expected


def test_3():
    roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]]
    seats = 2
    expected=  7
    assert Solution().minimumFuelCost(roads, seats) == expected