"""
LeetCode :: Grind 75 :: 110. Balanced Binary Tree
jramaswami
"""


class Solution:

    def isBalanced(self, root):

        def solve(node):
            if node is None:
                return True, 0

            left_ok, left_height = solve(node.left)
            right_ok, right_height = solve(node.right)
            my_height = 1 + max(left_height, right_height)
            my_ok = abs(left_height - right_height) <= 1 and left_ok and right_ok
            return my_ok, my_height

        return solve(root)[0]
