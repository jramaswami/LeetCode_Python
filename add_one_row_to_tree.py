"""
LeetCode :: October 2022 Challenge :: Add One Row To Tree
jramaswami
"""


class Solution:
    def addOneRow(self, root, val, depth):

        def rec(node, level):
            if node is None:
                return None

            if level == depth - 1:
                # Here is where we replace
                new_left = TreeNode(val, node.left)
                new_right = TreeNode(val, node.right)
                node.left = new_left
                node.right = new_right
                return node
            else:
                node.left = rec(node.left, level + 1)
                node.right = rec(node.right, level + 1)
                return node

        if depth == 1:
            return TreeNode(val, root, None)
        return rec(root, 1)
