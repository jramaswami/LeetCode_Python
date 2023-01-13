"""
LeetCode
2246. Longest Path With Different Adjacent Characters
January 2023 Challenge
jramaswami
"""


import heapq
from typing import *


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # Convert into graph.
        graph = [[] for _ in parent]
        for u, p in enumerate(parent[1:], start=1):
            graph[p].append(u)

        def traverse(u):
            """"
            Recursively traverse tree, getting the longest leg and
            longest path at each node.
            """
            my_longest_leg = my_longest_path = 1
            eligible_legs = []
            for v in graph[u]:
                # Get the longest leg and longest path from child v.
                their_longest_leg, their_longest_path = traverse(v)
                # See if their longest path is the longest one so far.
                my_longest_path = max(my_longest_path, their_longest_path)
                # If child v doesn't have the same letter as u ...
                if s[u] != s[v]:
                    # We might be able make a /\ path with u as the apex and
                    # the longest leg from v as a leg in the /\ path.
                    heapq.heappush(eligible_legs, their_longest_leg)
                    while len(eligible_legs) > 2:
                        heapq.heappop(eligible_legs)
                    # We can extend v's longest leg with u.
                    my_longest_leg = max(my_longest_leg, 1 + their_longest_leg)

            # Can we make a /\ path?  If so count it as the longest path.
            if len(eligible_legs) == 2:
                my_longest_path = max(my_longest_path, sum(eligible_legs) + 1)
            # Is the longest leg the longest path?
            my_longest_path = max(my_longest_path, my_longest_leg)

            return my_longest_leg, my_longest_path

        _, soln = traverse(0)
        return soln


def test_1():
    parent = [-1,0,0,1,1,2]
    s = "abacbe"
    expected = 3
    assert Solution().longestPath(parent, s) == expected


def test_2():
    parent = [-1,0,0,0]
    s = "aabc"
    expected = 3
    assert Solution().longestPath(parent, s) == expected