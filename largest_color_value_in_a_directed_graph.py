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
            path_colors[u_color] -= 1
            visited[u] = False
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


def test_4():
    "TLE"
    colors = "qddqqqddqqdqddddddqdqqddddqdqdqqdddqddqdqqdqqqqqddqddqqddqqqdqqqqdqdddddqdq"
    edges = [
        [0,1],[1,2],[2,3],[3,4],[3,5],[4,5],[3,6],[5,6],[6,7],[5,7],[3,7],
        [6,8],[5,8],[4,8],[8,9],[9,10],[10,11],[9,11],[9,12],[11,12],[6,12],
        [11,13],[9,13],[13,14],[12,14],[10,14],[11,14],[13,15],[14,15],[12,16],
        [9,16],[7,16],[15,17],[13,17],[17,18],[11,18],[17,19],[18,19],[13,19],
        [17,20],[18,20],[19,21],[17,21],[12,22],[21,22],[16,22],[22,23],
        [21,23],[16,24],[22,24],[15,25],[24,25],[20,25],[12,25],[23,26],
        [26,27],[13,27],[27,28],[21,28],[26,28],[28,29],[15,30],[27,30],
        [24,30],[21,30],[27,31],[30,31],[25,32],[29,32],[17,33],[31,33],
        [32,33],[25,34],[33,35],[31,35],[34,35],[30,36],[35,37],[36,37],
        [26,38],[36,38],[34,38],[37,38],[38,39],[22,39],[39,40],[40,41],
        [38,41],[20,41],[41,42],[37,42],[40,43],[42,43],[43,44],[41,44],
        [32,44],[38,44],[39,44],[43,45],[44,45],[44,46],[45,46],[45,47],
        [42,47],[43,48],[45,49],[45,50],[48,51],[30,51],[46,52],[48,52],
        [38,52],[51,52],[47,53],[45,53],[53,54],[48,54],[30,54],[50,55],
        [30,55],[36,55],[55,56],[39,56],[54,56],[50,57],[56,58],[32,58],
        [57,59],[49,59],[38,60],[60,61],[35,61],[54,61],[53,61],[54,62],
        [58,62],[62,63],[40,63],[58,63],[49,64],[63,64],[47,64],[39,64],
        [45,64],[62,65],[64,65],[54,65],[52,66],[61,66],[60,66],[55,67],
        [65,67],[45,68],[56,68],[36,68],[67,69],[66,69],[27,70],[60,70],
        [67,70],[48,71],[70,71],[53,71],[62,72],[72,73],[73,74]
    ]
    expected = 26
    assert Solution().largestPathValue(colors, edges) == expected