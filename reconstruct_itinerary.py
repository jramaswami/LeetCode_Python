"""
binarysearch.com :: Flight Itinerary Sequel
jramaswami
"""


import collections
import heapq


class Graph:

    def __init__(self):
        self.nodes = set()
        self.adj = collections.defaultdict(list)
        self.indegree = collections.defaultdict(int)
        self.outdegree = collections.defaultdict(int)
        self.path = []

    def add_edge(self, u, v):
        self.nodes.add(u)
        self.outdegree[u] += 1
        self.indegree[v] += 1
        self.nodes.add(v)
        self.adj[u].append(v)

    def _dfs(self, u):
        while self.outdegree[u] > 0:
            self.outdegree[u] -= 1
            i = self.outdegree[u]
            v = self.adj[u][i]
            self._dfs(v)
        self.path.append(u)

    def find_euler_path(self):
        for u in self.adj:
            self.adj[u].sort(reverse=True)
        root = "JFK"
        self._dfs(root)
        return self.path[::-1]


class Solution:

    def findItinerary(self, edges):
        graph = Graph()
        for u, v in edges:
            graph.add_edge(u, v)
        return graph.find_euler_path()


def test_1():
    tickets = [ ["YYZ", "SEA"], ["JFK", "YYZ"], ["SEA", "JFK"] ]
    expected = ["JFK", "YYZ", "SEA", "JFK"]
    assert Solution().findItinerary(tickets) == expected


def test_2():
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    expected = ["JFK","MUC","LHR","SFO","SJC"]
    assert Solution().findItinerary(tickets) == expected


def test_3():
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    expected = ["JFK","ATL","JFK","SFO","ATL","SFO"]
    assert Solution().findItinerary(tickets) == expected
