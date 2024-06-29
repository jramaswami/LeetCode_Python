"""
LeetCode
2192. All Ancestors of a Node in a Directed Acyclic Graph
June 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        soln = [[] for _ in range(n)]

        for root in range(n):
            queue = collections.deque()
            queue.append(root)
            visited = set()
            visited.add(root)
            while queue:
                u = queue.popleft()
                if root != u:
                    soln[u].append(root)
                for v in graph[u]:
                    if v not in visited:
                        queue.append(v)
                        visited.add(v)
        
        return soln
