"""
LeetCode ::  Is Graph Bipartite?
jramaswami
"""
from typing import *
from collections import deque, defaultdict


NONE = -1
BLACK = 0
WHITE = 1


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        queue = deque()
        color = defaultdict(lambda: NONE)
        color[0] = BLACK
        queue.append(0)
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if color[v] == NONE:
                    color[v] = (color[u] + 1) % 2
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True


def test_1():
    graph = [[1,3],[0,2],[1,3],[0,2]]
    assert Solution().isBipartite(graph) == True

def test_2():
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    assert Solution().isBipartite(graph) == False

def test_3():
    graph = [[]]
    assert Solution().isBipartite(graph) == True

def test_4():
    graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    assert Solution().isBipartite(graph) == False
