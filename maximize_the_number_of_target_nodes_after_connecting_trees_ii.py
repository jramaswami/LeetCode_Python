"""
LeetCode
3373. Maximize the Number of Target Nodes After Connecting Trees II
May 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        graph1 = collections.defaultdict(list)
        nodes1 = set()
        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
            nodes1.add(u)
            nodes1.add(v)

        graph2 = collections.defaultdict(list)
        nodes2 = set()
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)
            nodes2.add(u)
            nodes2.add(v)

        def bfs(root, graph):
            even_nodes = 0
            odd_nodes = 0
            visited = set()
            visited.add(root)
            queue = collections.deque()
            queue.append((root, 0))
            while queue:
                u, d = queue.popleft()
                if d % 2:
                    odd_nodes += 1
                else:
                    even_nodes += 1
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append((v, d + 1))
            return even_nodes, odd_nodes

        even_nodes1 = dict()
        odd_nodes1 = dict()
        for root in nodes1:
            evens, odds = bfs(root, graph1)
            even_nodes1[root] = evens
            odd_nodes1[root] = odds

        even_nodes2 = dict()
        odd_nodes2 = dict()
        for root in nodes2:
            evens, odds = bfs(root, graph2)
            even_nodes2[root] = evens
            odd_nodes2[root] = odds

        soln = [0 for _ in nodes1]
        for root1 in nodes1:
            for root2 in nodes2:
                soln[root1] = max(soln[root1], even_nodes1[root1] + odd_nodes2[root2])
        return soln


def test_1():
    edges1 = [[0,1],[0,2],[2,3],[2,4]]
    edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
    expected = [8,7,7,8,8]
    assert Solution().maxTargetNodes(edges1, edges2) == expected