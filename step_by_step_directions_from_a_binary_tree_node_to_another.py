"""
LeetCode
2096. Step-By-Step Directions From a Binary Tree Node to Another
July 2024 Challenge
jramaswami
"""


import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


Edge = collections.namedtuple('Edge', ['u', 'v', 'direction'])


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = collections.defaultdict(list)

        # Use DFS to build graph
        def build_graph(node):
            if node is None:
                return

            if node.left:
                graph[node.val].append(Edge(node.val, node.left.val, 'L'))
                graph[node.left.val].append(Edge(node.left.val, node.val, 'U'))
                build_graph(node.left)

            if node.right:
                graph[node.val].append(Edge(node.val, node.right.val, 'R'))
                graph[node.right.val].append(Edge(node.right.val, node.val, 'U'))
                build_graph(node.right)

        build_graph(root)

        # Use dfs to find route
        soln = ''
        visited = set()
        def find_route(node, path):
            visited.add(node)
            if node == destValue:
                nonlocal soln
                soln = ''.join(path)
            else:
                for edge in graph[node]:
                    if edge.v not in visited:
                        path.append(edge.direction)
                        find_route(edge.v, path)
                        path.pop()
            visited.remove(node)

        find_route(startValue, [])
        return soln