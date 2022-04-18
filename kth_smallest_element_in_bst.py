"""
LeetCode :: April 2022 Challenge :: 230. Kth Smallest Element in a BST
jramaswami
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        acc = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            acc.append(node.val)
            inorder(node.right)

        inorder(root)
        return acc[k-1]
