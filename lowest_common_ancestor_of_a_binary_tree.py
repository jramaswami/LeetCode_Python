"""
LeetCode :: June 2021 Challenge :: Lowest Common Ancestor of a Binary Tree
jramaswami
"""


class Solution():
    def lowestCommonAncestor(self, root, p_node, q_node):

        def dfs(node, parent, level):
            if node is None:
                return
            node.level = level
            node.parent = parent
            dfs(node.left, node, level + 1)
            dfs(node.right, node, level + 1)

        dfs(root, None, 0)

        while p_node.level > q_node.level:
            p_node = p_node.parent

        while q_node.level > p_node.level:
            q_node = q_node.parent

        while q_node != p_node:
            p_node = p_node.parent
            q_node = q_node.parent

        return p_node
