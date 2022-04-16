"""
LeetCode :: April 2022 Challenge :: 538. Convert BST to Greater Tree
jramaswami
"""


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def sum_right(node):
            if node is None:
                return 0

            right_subtree_sum = sum_right(node.right)
            left_subtree_sum = sum_right(node.left)

            node.val += right_subtree_sum
            return left_subtree_sum + node.val

        def push_left(node, acc):
            if node is None:
                return

            node.val += acc
            push_left(node.left, node.val)
            push_left(node.right, acc)


        sum_right(root)
        push_left(root, 0)
        return root
