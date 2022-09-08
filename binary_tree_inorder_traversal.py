"""
LeetCode :: September 2022 Challenge :: 94. Binary Tree Inorder Traversal
jramaswami
"""


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        soln = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            soln.append(node.val)
            inorder(node.right)
        inorder(root)
        return soln