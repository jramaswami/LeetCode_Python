"""
LeetCode :: January 2022 Challenge :: 1305. All Elements in Two Binary Search Trees
jramaswami


Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def getAllElements(self, root1, root2):

        def traverse(node, acc):
            if node is None:
                return
            acc.append(node.val)
            traverse(node.left, acc)
            traverse(node.right, acc)

        acc = []
        traverse(root1, acc)
        traverse(root2, acc)
        return sorted(acc)
