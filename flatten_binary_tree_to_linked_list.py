"""
Leet Code :: May 2021 Challenge :: Flatten Binary Tree to Linked List
jramaswami
"""
from typing import *


def flatten(node, preorder):
    """Flatten nodes into an array in preorder traversal."""
    if node is None:
        return
    preorder.append(node)
    flatten(node.left, preorder)
    flatten(node.right, preorder)
    node.left = None
    node.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Flatten the array into preorder traversal.
        preorder = []
        flatten(root, preorder[1:])
        # Reconnect all the nodes leaning right.
        node = root
        for right in preorder:
            node.right = right
            node = right
        return root
