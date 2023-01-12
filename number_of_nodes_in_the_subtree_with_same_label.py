"""
LeetCode
1519. Number of Nodes in the Sub-Tree With the Same Label
January 2023 Challenge
"""


import collections
from typing import *


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for _ in labels]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        soln = [0 for _ in labels]

        def traverse(u, p):
            my_labels = collections.Counter()

            for v in graph[u]:
                if v != p:
                    my_labels.update(traverse(v, u))
            my_labels[labels[u]] += 1
            soln[u] = my_labels[labels[u]]
            return my_labels

        _ = traverse(0, -1)
        return soln


def test_1():
    n = 7
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    labels = "abaedcd"
    expected = [2,1,1,1,1,1,1]
    assert Solution().countSubTrees(n, edges, labels) == expected


def test_2():
    n = 4
    edges = [[0,1],[1,2],[0,3]]
    labels = "bbbb"
    expected = [4,2,1,1]
    assert Solution().countSubTrees(n, edges, labels) == expected


def test_3():
    n = 5
    edges = [[0,1],[0,2],[1,3],[0,4]]
    labels = "aabab"
    expected = [3,2,1,1,1]
    assert Solution().countSubTrees(n, edges, labels) == expected