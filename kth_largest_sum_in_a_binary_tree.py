"""
LeetCode
2583. Kth Largest Sum in a Binary Tree
October 2024 Challenge
jramaswami
"""


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        level_sums = []

        def rec(node, i):
            if node is None:
                return

            while len(level_sums) <= i:
                level_sums.append(0)
            
            level_sums[i] += node.val
            rec(node.left, i+1)
            rec(node.right, i+1)

        rec(root, 0)
        level_sums.sort(reverse=True)
        k -= 1
        if len(level_sums) <= k:
            return -1
        return level_sums[k]
