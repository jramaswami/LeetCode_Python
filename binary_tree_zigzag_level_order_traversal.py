"""
LeetCode
103. Binary Tree Zigzag Level Order Traversal
February 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        soln = [[root] if root else []]
        level = 0
        while soln[-1]:
            T = []
            for node in reversed(soln[-1]):
                if level % 2:
                    if node.left:
                        T.append(node.left)
                    if node.right:
                        T.append(node.right)
                else:
                    if node.right:
                        T.append(node.right)
                    if node.left:
                        T.append(node.left)
            soln.append(T)
            level += 1
        soln.pop()
        return [[node.val for node in row] for row in soln]
