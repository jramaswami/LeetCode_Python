"""
LeetCode
103. Binary Tree Zigzag Level Order Traversal
February 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        soln = []
        def inorder(node, level):
            if node is None:
                return
            while len(soln) <= level:
                soln.append([])

            soln[level].append(node.val)
            inorder(node.left, level+1)
            inorder(node.right, level+1)

        inorder(root, 0)
        for i, _ in enumerate(soln):
            if i % 2:
                soln[i] = soln[i][::-1]
        return soln