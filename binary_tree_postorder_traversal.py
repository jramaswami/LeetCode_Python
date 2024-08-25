"""
LeetCode
145. Binary Tree Postorder Traversal
August 2024 Challenge
jramaswami
"""


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        soln = []

        def rec(node):
            if node is None:
                return
            rec(node.left)
            rec(node.right)
            soln.append(node.val)

        rec(root)
        return soln
