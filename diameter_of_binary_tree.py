"""
LeetCode :: October 2021 Challenge :: 543. Diameter of Binary Tree
jramaswami
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            """DFS to find the maximum number of edges and maximum path for subtree."""
            if node is None:
                return 0, 0

            left_edges, left_path = dfs(node.left)
            right_edges, right_path = dfs(node.right)

            max_edges = 1 + max(left_edges, right_edges)
            max_path = max(left_path, right_path, right_edges + left_edges)
            return max_edges, max_path

        return dfs(root)[1]
