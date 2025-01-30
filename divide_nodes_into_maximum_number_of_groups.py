"""
LeetCode
2493. Divide Nodes Into the Maximum Number of Groups
January 2025 Challenge
jramaswami
"""


import collections
from typing import List


def is_bipartite(graph):
    """Return True if graph is bipartite, False if it is not
    """
    # Colors for bipartiteness
    WHITE, RED, BLUE = 0, 1, 2
    color = {x: WHITE for x in graph}

    def other_color(curr_color):
        if curr_color == RED:
            return BLUE
        return RED

    for root in color:
        if color[root] == WHITE:
            # Unvisited node, start BFS from here
            color[root] = RED
            queue = collections.deque()
            queue.append(root)
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == color[u]:
                        # Graph is not bipartite
                        return False
                    elif color[v] == WHITE:
                        # Unvisited node
                        color[v] = other_color(color[u])
                        queue.append(v)
    return True


def identify_components(graph):
    """Group the nodes by root returning a list of ids
    """
    component_ids = dict()
    for root in graph:
        if root not in component_ids:
            # Not visited yet, BFS to find all nodes in this component
            queue = collections.deque()
            queue.append(root)
            component_ids[root] = root
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in component_ids:
                        # Not visited, assign group and add to queue
                        queue.append(v)
                        component_ids[v] = root
    return component_ids


def get_max_depth(graph, root):
    queue = collections.deque()
    visited = set()
    visited.add(root)
    queue.append((root, 1))
    max_depth = 0
    while queue:
        u, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append((v, depth+1))
    return max_depth


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Turn edge list into adjacency list
        graph = {x: [] for x in range(1, n+1)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Make sure graph is bipartite
        if not is_bipartite(graph):
            return -1

        # Assign nodes to groups
        component_ids = identify_components(graph)

        # Try each node for max for group
        max_depths = collections.defaultdict(int)
        for root in graph:
            component_id = component_ids[root]
            max_depth = get_max_depth(graph, root)
            max_depths[component_id] = max(max_depths[component_id], max_depth)
        return sum(max_depths.values())


def test_1():
    n = 6
    edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
    expected = 4
    assert Solution().magnificentSets(n, edges) == expected


def test_2():
    n = 3
    edges = [[1,2],[2,3],[3,1]]
    expected =  -1
    assert Solution().magnificentSets(n, edges) == expected
