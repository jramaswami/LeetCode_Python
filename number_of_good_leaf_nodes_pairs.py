"""
LeetCode
1530. Number of Good Leaf Nodes Pairs
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


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = collections.defaultdict(list)
        leaf_nodes = set()

        def make_graph(node, parent):
            if node is None:
                return

            if node.left is None and node.right is None:
                leaf_nodes.add(node)

            if parent:
                graph[parent].append(node)
                graph[node].append(parent)

            make_graph(node.left, node)
            make_graph(node.right, node)

        make_graph(root, None)

        soln = 0

        def find_pairs(current, previous, steps):
            if previous and current in leaf_nodes:
                nonlocal soln
                soln += 1

            for neighbor in graph[current]:
                if neighbor != previous and steps + 1 <= distance:
                    find_pairs(neighbor, current, steps + 1)

        for leaf_node in leaf_nodes:
            find_pairs(leaf_node, None, 0)
        return soln // 2