"""
LeetCode
1161. Maximum Level Sum of a Binary Tree
June 2023 Challenge
jramaswami
"""


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []

        def rec(node, level):
            if node is None:
                return

            if level == len(sums):
                sums.append(0)

            sums[level] += node.val
            rec(node.left, level+1)
            rec(node.right, level+1)

        # Compute the level sums.
        rec(root, 0)
        # Find the maximum level sum.
        max_sum = max(sums)
        return 1 + sums.index(max_sum)