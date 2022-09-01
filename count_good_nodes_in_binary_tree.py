"""
LeetCode :: September 2022 Challenge :: 1448. Count Good Nodes in Binary Tree
jramaswami
"""


import math


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def solve(node: TreeNode, prev_max: int) -> int:
            if node is None:
                return 0

            result = (1 if node.val >= prev_max else 0)
            new_max = max(prev_max, node.val)
            return result + solve(node.left, new_max) + solve(node.right, new_max)

        return solve(root, -math.inf)
