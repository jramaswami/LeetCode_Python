"""
LeetCode
144. Binary Tree Preorder Traversal
January 2023 Challenge
jramaswami
"""


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        soln = []

        def preorder(node):
            if node is None:
                return
            soln.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return soln