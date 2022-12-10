"""
LeetCode
1339. Maximum Product of Splitted Binary Tree
December 2022 Challenge
jramaswami
"""


import math


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def augment_with_sum(node):
            if node is None:
                return 0
            node.sum = (
                    node.val +
                    augment_with_sum(node.left) +
                    augment_with_sum(node.right)
            )
            return node.sum

        def get_max_product(node, root_sum):
            if node is None:
                return -math.inf
            return max(
                    get_max_product(node.left, root_sum),
                    get_max_product(node.right, root_sum),
                    (node.sum * (root_sum - node.sum))
            )

        augment_with_sum(root)
        return get_max_product(root, root.sum) % (pow(10, 9) + 7)
