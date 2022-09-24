"""
LeetCode :: September 2022 Challenge :: Path Sum II
jramaswami
"""


class Solution:
    def pathSum(self, root, target_sum):
        soln = []

        def is_leaf(node):
            return node.left is None and node.right is None

        def dfs(node, acc, curr_sum):
            if node is None:
                return

            acc.append(node.val)
            curr_sum += node.val

            if is_leaf(node):
                if curr_sum == target_sum:
                    soln.append(list(acc))
            else:
                dfs(node.left, acc, curr_sum)
                dfs(node.right, acc, curr_sum)

            acc.pop()

        dfs(root, [], 0)
        return soln