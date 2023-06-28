"""
LeetCode
1514. Path with Maximum Probability
June 2023 Challenge
jramaswami
"""


import collections
import heapq
from typing import List


Edge = collections.namedtuple('Edge', ['neighbor', 'prob'])
QItem = collections.namedtuple('QItem', ['negprob', 'node'])


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Create adjacency list
        graph = [[] for _ in range(n)]
        for [u, v], p in zip(edges, succProb):
            graph[u].append(Edge(v, p))
            graph[v].append(Edge(u, p))

        probs = [0.0 for _ in range(n)]
        queue = [QItem(-1, start)]
        while queue:
            item = heapq.heappop(queue)
            for edge in graph[item.node]:
                prob = (-item.negprob) * edge.prob
                if prob > probs[edge.neighbor]:
                    probs[edge.neighbor] = prob
                    heapq.heappush(queue, QItem(-prob, edge.neighbor))
        return probs[end]


EPS = pow(10,-5)


def test_1():
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start = 0
    end = 2
    expected = 0.25
    assert abs(Solution().maxProbability(n, edges, succProb, start, end) - expected) < EPS
    

def test_2():
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.3]
    start = 0
    end = 2
    expected = 0.3
    assert abs(Solution().maxProbability(n, edges, succProb, start, end) - expected) < EPS


def test_3():
    n = 3
    edges = [[0,1]]
    succProb = [0.5]
    start = 0
    end = 2
    expected = 0.0
    assert abs(Solution().maxProbability(n, edges, succProb, start, end) - expected) < EPS
