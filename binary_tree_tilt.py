"""
LeetCode :: December 2021 Challenge :: 563. Binary Tree Tilt
jramaswami
"""


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        def traverse(node):
            if node is None:
                return 0, 0

            left_val_sum, left_tilt_sum = traverse(node.left)
            right_val_sum, right_tilt_sum = traverse(node.right)

            my_tilt = abs(left_val_sum - right_val_sum)
            my_val_sum = node.val + left_val_sum + right_val_sum
            my_tilt_sum = my_tilt + left_tilt_sum + right_tilt_sum

            return my_val_sum, my_tilt_sum

        return traverse(root)[1]
