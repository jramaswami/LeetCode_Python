"""
LeetCode
951. Flip Equivalent Binary Trees
October 2024 Challenge
jramaswami
"""


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def rec(x, y):
            if (x is None) and (y is None):
                return True
            
            if x is None or y is None:
                return False

            if x.val != y.val:
                return False
            
            if x.left is None and y.left is None:
                # Do not flip
                return rec(x.left, y.left) and rec(x.right, y.right)
            elif x.left is None or y.left is None:
                # Flip
                return rec(x.left, y.right) and rec(x.right, y.left)
            if x.left.val != y.left.val:
                # Flip
                return rec(x.left, y.right) and rec(x.right, y.left)
            # Do not flip
            return rec(x.left, y.left) and rec(x.right, y.right)

        return rec(root1, root2)
