"""
LeetCode
2097. Valid Arrangement of Pairs
November 2024 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=093ICzicTmg
"""

import collections


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        outdegree = collections.defaultdict(int)
        nodes = set()
        for u, v in pairs:
            nodes.add(u)
            nodes.add(v)
            graph[u].append(v)
            outdegree[u] += 1
            indegree[v] += 1
        
        # Start with the node with outdegree - indegree == 1 otherwise any point
        starting_node = min(nodes)
        for node in nodes:
            if outdegree[node] - indegree[node] == 1:
                starting_node = node
                break

        # Run DFS
        soln = []
        def dfs(u):
            while graph[u]:
                v = graph[u].pop()
                dfs(v)
                soln.append([u, v])
        dfs(starting_node)
        return soln[::-1]
