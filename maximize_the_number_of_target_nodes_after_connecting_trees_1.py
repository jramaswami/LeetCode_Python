"""
LeetCode
3372. Maximize the Number of Target Nodes After Connecting Trees I
May 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
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

        def bfs(root, graph, max_dist):
            visited = set()
            visited.add(root)
            queue = collections.deque()
            queue.append((root, 0))
            while queue:
                u, d = queue.popleft()
                for v in graph[u]:
                    if d + 1 <= max_dist:
                        visited.add(v)
                        queue.append((v, d + 1))
            return len(visited)


        target1 = dict()
        for root in nodes1:
            target1[root] = bfs(root, graph1, k)

        target2 = dict()
        for root in nodes2:
            target2[root] = bfs(root, graph2, k-1)

        soln = [0 for _ in nodes1]
        for root1 in nodes1:
            for root2 in nodes2:
                soln[root1] = max(soln[root1], target1[root1] + target2[root2])
        return soln


def test_1():
    edges1 = [[0,1],[0,2],[2,3],[2,4]]
    edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
    k = 2
    expected = [9,7,9,8,8]
    assert Solution().maxTargetNodes(edges1, edges2, k) == expected



def test_3():
    "WA"
    edges1 = [[0,1]]
    edges2 = [[0,1]]
    k = 0
    expected = [1,1]
    assert Solution().maxTargetNodes(edges1, edges2, k) == expected