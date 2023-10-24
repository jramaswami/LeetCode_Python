"""
LeetCode
515. Find Largest Value in Each Tree Row
October 2023 Challenge
jramaswami
"""


import math


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        soln = []

        def rec(node, level):
            if node is None:
                return

            while level >= len(soln):
                soln.append(-math.inf)

            soln[level] = max(soln[level], node.val)
            rec(node.left, level+1)
            rec(node.right, level+1)

        rec(root, 0)
        return soln