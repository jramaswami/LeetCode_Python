"""
LeetCode :: April 2022 Challenge :: 669. Trim a Binary Search Tree
jramaswami
"""


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None

        left_subtree = self.trimBST(root.left, low, high)
        right_subtree = self.trimBST(root.right, low, high)

        if low <= root.val <= high:
            root.left = left_subtree
            root.right = right_subtree
            return root

        # root must be removed.
        if left_subtree is None:
            return right_subtree
        elif right_subtree is None:
            return left_subtree
        else:
            # The left subtree contains values less than right subtree.
            # The easiest thing to do is put the left subtree at the
            # bottom of the right subtree.
            curr = right_subtree
            while curr.left is not None:
                curr = curr.left
            curr.left = left_subtree
            return right_subtree
