"""
LeetCode
872. Leaf-Similar Trees
December 2022 Challenge
jramaswami
"""


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def is_leaf(node):
            return node.left is None and node.right is None

        def inorder(node, acc):
            if node is None:
                return

            inorder(node.left, acc)
            if is_leaf(node):
                acc.append(node.val)
            inorder(node.right, acc)

        left = []
        right = []
        inorder(root1, left)
        inorder(root2, right)
        return left == right
