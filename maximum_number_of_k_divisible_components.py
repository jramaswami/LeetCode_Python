"""
LeetCode
2872. Maximum Number of K-Divisible Components
December 2024 Challenge
jramaswami

Thank You NeetCode.IO!
"""


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        assert sum(values) % k == 0
        # Turn edges into graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        result = 0

        def dfs(curr, parent):
            total = values[curr]
            for child in graph[curr]:
                if child != parent:
                    total += dfs(child, curr)
            
            if total % k == 0:
                nonlocal result
                result += 1
            return total
            
        dfs(0, -1)
        return result
