"""
LeetCode :: April 2022 Challenge :: 99. Recover Binary Search Tree
"""


class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []

        def inorder(node):
            if node is not None:
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)

        inorder(root)
        nodes0 = sorted(n.val for n in nodes)
        for a, b in zip(nodes, nodes0):
            if a.val != b:
                a.val = b
