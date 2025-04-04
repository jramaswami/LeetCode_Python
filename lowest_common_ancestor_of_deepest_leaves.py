"""
LeetCode
1123. Lowest Common Ancestor of Deepest Leaves
April 2025 Challenge
jramaswami

Thank You NeetCode.IO
"""


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Return (LCA, height)
        def dfs(node):
            if not node:
                return (None, 0)
            left_node, left_height = dfs(node.left)
            right_node, right_height = dfs(node.right)

            if left_height == right_height:
                return node, 1 + left_height
            elif left_height > right_height:
                return left_node, left_height + 1
            else:
                return right_node, right_height + 1

        node, _ = dfs(root)
        return node