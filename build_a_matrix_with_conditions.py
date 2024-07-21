"""
LeetCode
2392. Build a Matrix With Conditions
July 2024 Challenge
jramaswami
"""


import collections
from typing import List


WHITE = 0
GRAY = 1
BLACK = 2


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Create digraph for row conditions
        row_graph = collections.defaultdict(list)
        for u, v in rowConditions:
            row_graph[u].append(v)

        # Create digraph for column conditions
        col_graph = collections.defaultdict(list)
        for u, v in colConditions:
            col_graph[u].append(v)

        # Topological sort function
        def topo(graph):
            toposort = collections.deque()
            color = [WHITE for _ in range(k+1)]

            def visit(u):
                if color[u] == BLACK:
                    return
                if color[u] == GRAY:
                    raise Exception('Graph is not acyclic')
                color[u] = GRAY
                for v in graph[u]:
                    visit(v)
                color[u] = BLACK
                toposort.appendleft(u)

            for root in range(1,k+1):
                if color[root] == WHITE:
                    visit(root)
            return toposort

        # Topological sort by row to assign rows
        try:
            row_indices = {x: r for r, x in enumerate(topo(row_graph))}
            col_indices = {x: c for c, x in enumerate(topo(col_graph))}
        except:
            return []

        matrix = [[0 for _ in range(k)] for _ in range(k)]
        for x in range(1, k+1):
            r = row_indices[x]
            c = col_indices[x]
            matrix[r][c] = x
        return matrix



def check(matrix, rowConditions, colConditions):
    # Get posns
    posns = {}
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if val != 0:
                posns[val] = (r, c)

    for u, v in rowConditions:
        if posns[u][0] >= posns[v][0]:
            print(f'{u}@row{posns[u][0]}, {v}@row{posns[v][0]}')
            return False
    for u, v in colConditions:
        if posns[u][1] >= posns[v][1]:
            print(f'{u}@col{posns[u][1]}, {v}@col{posns[v][1]}')
            return False

    return len(posns) == len(matrix)


def test_1():
    k = 3
    rowConditions = [[1,2],[3,2]]
    colConditions = [[2,1],[3,2]]
    result = Solution().buildMatrix(k, rowConditions, colConditions)
    assert check(result, rowConditions, colConditions)