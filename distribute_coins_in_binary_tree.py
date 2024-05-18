"""
LeetCode
979. Distribute Coins in Binary Tree
jramaswami

Thank You NeetCode.IO
"""


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.soln = 0

        def rec(node):
            if node is None:
                return 0, 0

            left_size, left_coins = rec(node.left)
            right_size, right_coins = rec(node.right)
            my_size, my_coins = left_size + right_size + 1, left_coins + right_coins + node.val

            self.soln += abs(my_size - my_coins)
            return my_size, my_coins

        rec(root)
        return self.soln