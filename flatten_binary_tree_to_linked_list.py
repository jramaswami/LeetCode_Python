"""
Leet Code :: July 2022 Challenge :: Flatten Binary Tree to Linked List
jramaswami
"""


from typing import *
from leetcode_trees import *


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Boundary case.
        if root is None:
            return None

        # Create a list of nodes inorder.
        inorder = []
        def traverse(node):
            if node is None:
                return

            inorder.append(node)
            traverse(node.left)
            traverse(node.right)

        traverse(root)

        print(inorder)

        # Fix the nodes in the list.
        for a, b in zip(inorder[:-1], inorder[1:]):
            a.left, a.right = None, None
            b.left, b.right = None, None
            a.right = b
        return inorder[0]
