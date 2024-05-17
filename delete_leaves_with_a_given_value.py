"""
LeetCode
1325. Delete Leaves With a Given Value
May 2024 Challenge
jramaswami
"""


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def is_leaf(node):
            return node.left is None and node.right is None

        def rec(node):
            if node is None:
                return None

            node.left = rec(node.left)
            node.right = rec(node.right)

            if is_leaf(node) and node.val == target:
                return None
            return node

        return rec(root)