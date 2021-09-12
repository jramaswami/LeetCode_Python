"""
LeetCode :: September 2021 Challenge :: Reachable Nodes In Subdivided Graph
jramaswami
"""


from collections import defaultdict, namedtuple
from itertools import combinations


Edge = namedtuple('Edge', ['node_id', 'subnodes'])


class Solution:

    def reachableNodes(self, edges, max_moves, node_count):

        # Convert edges to adjacency list and list of weights.
        adj = defaultdict(list)
        weights = defaultdict(int)
        for u, v, w in edges:
            adj[u].append(Edge(v, w))
            adj[v].append(Edge(u, w))
            weights[min(u, v), max(u, v)] = w

        # Keep track of how many subnodes were crossed from any u to v.
        crossed = defaultdict(int)

        # Keep track of nodes that are reached.
        reached = set()

        # DFS to count how far.
        def dfs(node, moves):
            reached.add(node)
            for neighbor in adj[node]:
                # Given the number of moves remaining can I cross?
                key = (node, neighbor.node_id)
                if moves > neighbor.subnodes:
                    # If I can cross, marked all subnodes as crossed
                    # and continue to the next node after subtracting
                    # the number of moves to cross.
                    crossed[key] = neighbor.subnodes
                    dfs(neighbor.node_id, moves - neighbor.subnodes - 1)
                else:
                    # If I cannot cross, count the number of subnodes I
                    # can get to and stop.
                    crossed[key] = max(crossed[key], moves)

        dfs(0, max_moves)

        # Count the number of nodes that were reached.
        soln = len(reached)
        # Count the number of subnodes that were reached.
        for u, v in combinations(reached, 2):
            key = (min(u, v), max(u, v))
            soln += min(crossed[(u, v)] + crossed[(v, u)], weights[key])
        return soln


def test_1():
    edges = [[0,1,10],[0,2,1],[1,2,2]]
    max_moves = 6
    node_count = 3
    assert Solution().reachableNodes(edges, max_moves, node_count) == 13


def test_2():
    edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]]
    max_moves = 10
    node_count = 4
    assert Solution().reachableNodes(edges, max_moves, node_count) == 23


def test_3():
    edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]]
    max_moves = 17
    node_count = 5
    assert Solution().reachableNodes(edges, max_moves, node_count) == 1


def test_4():
    """WA"""
    edges = [[1,2,5],[0,3,3],[1,3,2],[2,3,4],[0,4,1]]
    max_moves = 7
    node_count = 5
    assert Solution().reachableNodes(edges, max_moves, node_count) == 13


