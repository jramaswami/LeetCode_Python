"""
LeetCode :: November 2021 Challenge :: 106. Construct Binary Tree from Inorder and Postorder Traversal
jramaswami
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder, postorder):

        def solve(I, P):
            # Base case:
            if not P:
                return None
            # In the postorder, P, the last item is the root of this subtree.
            root = TreeNode(P[-1])
            # Find P[-1] in the inorder, I.
            i = I.index(P[-1])
            # Recurse
            root.left = solve(I[:i], P[:i])
            root.right = solve(I[i+1:], P[i:-1])
            return root

        return solve(inorder, postorder)