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

        graph2 = collections.defaultdict(list)
        nodes2 = set()
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        def color_graph(root, graph):
            even_nodes = 0
            odd_nodes = 0
            colors = dict()
            visited = set()
            visited.add(root)
            queue = collections.deque()
            queue.append((root, 0))
            while queue:
                u, d = queue.popleft()
                colors[u] = d % 2
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append((v, d + 1))
            return colors

        root1 = edges1[0][0]
        root2 = edges2[0][0]
        colors1 = color_graph(root1, graph1)
        colors2 = color_graph(root2, graph2)
        odds1 = evens1 = 0
        for color in colors1.values():
            if color:
                odds1 += 1
            else:
                evens1 += 1

        odds2 = evens2 = 0
        for color in colors2.values():
            if color:
                odds2 += 1
            else:
                evens2 += 1
        max_from2 = max(odds2, evens2)

        soln = [0 for _ in colors1]
        for root1, color in colors1.items():
            if color % 2:
                soln[root1] = odds1 + max_from2
            else:
                soln[root1] = evens1 + max_from2
        return soln


def test_1():
    edges1 = [[0,1],[0,2],[2,3],[2,4]]
    edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
    expected = [8,7,7,8,8]
    assert Solution().maxTargetNodes(edges1, edges2) == expected