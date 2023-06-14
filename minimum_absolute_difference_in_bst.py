"""
LeetCode
530. Minimum Absolute Difference in BST
June 2023 Challenge
jramaswami
"""


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def inorder(node, acc):
            if node is None:
                return

            inorder(node.left, acc)
            acc.append(node.val)
            inorder(node.right, acc)

        values = []
        inorder(root, values)
        return min(b-a for a, b in zip(values[:-1], values[1:]))
