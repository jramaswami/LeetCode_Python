"""
LeetCode
1857. Largest Color Value in a Directed Graph
April 2023 Challenge
jramaswami
"""


from typing import *
import collections


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        in_degree = [0 for _ in colors]
        graph = [[] for _ in colors]
        for u, v in edges:
            in_degree[v] += 1
            graph[u].append(v)

        soln = collections.Counter()

        def dfs(u, visited, path_colors):
            print(f"dfs({u=} {path_colors=} {visited=})")
            # Found a cycle.
            if visited[u]:
                return True
            u_color = colors[u]
            path_colors[u_color] += 1
            soln[u_color] = max(soln[u_color], path_colors[u_color])
            visited[u] = True
            for v in graph[u]:
                if dfs(v, visited, path_colors):
                    return True
            return False

        # Start with nodes that have an in_degree of zero.
        # If there aren't any there is a cycle.
        if all(d > 0 for d in in_degree):
            return -1

        for root, _ in enumerate(colors):
            if in_degree[root] == 0:
                # Root node for dfs.
                path_colors = collections.Counter()
                visited = [False for _ in colors]
                cycle_exists = dfs(root, visited, path_colors)
                if cycle_exists:
                    return -1

        return max(soln.values())




def test_1():
    colors = "abaca"
    edges = [[0,1],[0,2],[2,3],[3,4]]
    expected = 3
    assert Solution().largestPathValue(colors, edges) == expected


def test_2():
    colors = "a"
    edges = [[0,0]]
    expected = -1
    assert Solution().largestPathValue(colors, edges) == expected


def test_3():
    "WA"
    colors = "hhqhuqhqff"
    edges = [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]
    expected = 3
    assert Solution().largestPathValue(colors, edges) == expected