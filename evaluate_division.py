"""
LeetCode :: April 2022 Challenge :: 399. Evaluate Division
jramaswami
"""


import collections


class Solution:

    def calcEquation(self, equations, values, queries):

        def query(a, z, graph):
            if z in graph:
                Q = collections.deque()
                Q.append((a, 1.0))
                visited = set()
                visited.add(a)
                while Q:
                    u, w = Q.popleft()
                    if u == z:
                        return w
                    for v in graph[u]:
                        if v not in visited:
                            w0 = w * graph[u][v]
                            Q.append((v, w0))
                            visited.add(v)
            return -1.0

        graph = collections.defaultdict(dict)
        for (u, v), w in zip(equations, values):
            graph[u][v] = w
            graph[v][u] = 1.0 / w

        return [query(a, b, graph) for a, b in queries]


def test_1():
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    expected = [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    assert Solution().calcEquation(equations, values, queries) == expected


def test_2():
    equations = [["a","b"],["b","c"],["bc","cd"]]
    values = [1.5,2.5,5.0]
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    expected = [3.75000,0.40000,5.00000,0.20000]
    assert Solution().calcEquation(equations, values, queries) == expected


def test_3():
    equations = [["a","b"]]
    values = [0.5]
    queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    expected = [0.50000,2.00000,-1.00000,-1.00000]
    assert Solution().calcEquation(equations, values, queries) == expected
