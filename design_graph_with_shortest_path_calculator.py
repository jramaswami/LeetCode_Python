"""
LeetCode
2642. Design Graph With Shortest Path Calculator
November 2023 Challenge
jramaswami
"""


from typing import List
import collections
import heapq
import math


Edge = collections.namedtuple('Edge', ['u', 'v', 'wt'])
QItem = collections.namedtuple('QItem', ['dist', 'u'])


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = collections.defaultdict(list)
        self.n = n
        for e in edges:
            self.addEdge(e)

    def addEdge(self, edge: List[int]) -> None:
        e = Edge(*edge)
        self.adj[e.u].append(e)

    def shortestPath(self, node1: int, node2: int) -> int:
        queue = [QItem(0, node1)]
        dist = collections.defaultdict(lambda: math.inf)
        dist[node1] = 0
        while queue:
            item = heapq.heappop(queue)
            if item.u == node2:
                return item.dist
            if item.dist > dist[item.u]:
                continue
            for edge in self.adj[item.u]:
                item0 = QItem(item.dist + edge.wt, edge.v)
                heapq.heappush(queue, item0)
                dist[edge.v] = min(dist[edge.v], item0.dist)
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)