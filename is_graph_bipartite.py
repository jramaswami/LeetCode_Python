"""
LeetCode :: April 2022 Challenge :: 785. Is Graph Bipartite?
jramaswami
"""


import collections


BLACK = 0
WHITE = 1
GRAY = -1


class Solution:

    def isBipartite(self, graph):
        color = [GRAY for _ in graph]
        for root, _ in enumerate(graph):
            if color[root] == GRAY:
                Q = collections.deque()
                Q.append(root)
                color[root] = WHITE
                while Q:
                    u = Q.popleft()
                    for v in graph[u]:
                        if color[v] == color[u]:
                            return False
                        elif color[v] == GRAY:
                            color[v] = (BLACK if color[u] == WHITE else WHITE)
                            Q.append(v)
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


def test_5():
    graph = [[4],[],[4],[4],[0,2,3]]
    assert Solution().isBipartite(graph) == True
