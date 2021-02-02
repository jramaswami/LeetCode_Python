"""
LeetCode :: Trim a Binary Search Tree
jramaswami
"""
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root == None:
            return root

        if root.val < low:
            # All values to my left are less than me, so they will
            # also be out of the interval.  That means I should be
            # the right subtree after if is fixed.
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            # Same thing for the right
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
