"""
LeetCode :: September 2022 Challenge :: 606. Construct String from Binary Tree
jramaswami
"""


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = []

        def traverse(node):
            result.append('(')
            if node:
                result.append(str(node.val))
                if node.left or node.right:
                    traverse(node.left)
                if node.right:
                    traverse(node.right)
            result.append(')')

        traverse(root)
        return "".join(result[1:-1])