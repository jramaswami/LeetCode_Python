"""
LeetCode :: September 2022 Challenge :: 814. Binary Tree Pruning
jramaswami
"""


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def traverse(node):
            if node is None:
                return False, None

            left_result, left_node = traverse(node.left)
            right_result, right_node = traverse(node.right)

            if node.val == 1 or left_result or right_result:
                return True, TreeNode(node.val, left_node, right_node)
            return False, None

        return traverse(root)[1]