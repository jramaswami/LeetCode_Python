"""
LeetCode :: September 2022 Challenge :: 987. Vertical Order Traversal of a Binary Tree
jramaswami
"""


import collections


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        values = collections.defaultdict(list)

        def traverse(node, index, level):
            if node is None:
                return
            values[index].append((level, node.val))
            traverse(node.left, index - 1, level + 1)
            traverse(node.right, index + 1, level + 1)

        traverse(root, 0, 0)
        soln = []
        for k in sorted(values):
            soln.append([t[1] for t in sorted(values[k])])
        return soln