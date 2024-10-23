"""
LeetCode
2641. Cousins in Binary Tree II
October 2024 Challenge
jramaswami
"""


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        level_sums = []

        def dfs1(node, level):
            if node is None:
                return
            
            while len(level_sums) <= level:
                level_sums.append(0)
            
            level_sums[level] += node.val
            dfs1(node.left, level+1)
            dfs1(node.right, level+1)

        
        def dfs2(node, level):
            if node is None:
                return

            sibling_sum = 0
            if node.left:
                sibling_sum += node.left.val
            if node.right:
                sibling_sum += node.right.val
            if node.left:
                node.left.val = level_sums[level+1] - sibling_sum
            if node.right:
                node.right.val = level_sums[level+1] - sibling_sum
            dfs2(node.left, level+1)
            dfs2(node.right, level+1)

        dfs1(root, 0)
        dfs2(root, 0)
        root.val = 0
        return root
