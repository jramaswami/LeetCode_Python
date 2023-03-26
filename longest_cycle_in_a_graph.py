"""
LeetCode
2360. Longest Cycle in a Graph
March 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [False for _ in edges]
        in_path = [-1 for _ in edges]
        self.soln = -1

        def dfs(u, path_length):
            if in_path[u] >= 0:
                print(in_path)
                self.soln = max(self.soln, path_length - in_path[u])
            else:
                visited[u] = True
                in_path[u] = path_length
                if edges[u] >= 0:
                    dfs(edges[u], path_length + 1)
                in_path[u] = -1

        for root, _ in enumerate(edges):
            if not visited[root]:
                print(root)
                dfs(root, 1)
        return self.soln


def test_1():
    edges = [3,3,4,2,3]
    expected = 3
    assert Solution().longestCycle(edges) == expected


def test_2():
    edges = [2,-1,3,1]
    expected = -1
    assert Solution().longestCycle(edges) == expected