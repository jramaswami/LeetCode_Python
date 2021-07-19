"""
LeetCode :: July 2021 Challenge :: Lowest Common Ancestor of a Binary Search Tree
jramaswami
"""


class Solution:
    def lowestCommonAncestor(self, root, p, q):

        prev_node = root
        right_node = root
        left_node = root

        # Search for p and q simultaneously.  When they diverge, the last
        # node where they were the same is the LCA.
        while left_node == right_node:

            prev_node = left_node

            if p.val < left_node.val:
                left_node = left_node.left
            elif p.val == left_node.val:
                pass
            elif p.val > left_node.val:
                left_node = left_node.right

            if q.val < right_node.val:
                right_node = right_node.left
            elif q.val == right_node.val:
                pass
            elif q.val > right_node.val:
                right_node = right_node.right

        return prev_node
