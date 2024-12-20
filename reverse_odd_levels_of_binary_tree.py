"""
LeetCode
2415. Reverse Odd Levels of Binary Tree
December 2024 Challenge
jramaswami
"""


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        levels = []
        def rec(node, level):
            if node is not None:
                while len(levels) <= level:
                    levels.append([])
                levels[level].append(node)
                rec(node.left, level+1)
                rec(node.right, level+1)
                node.left = None
                node.right = None

        rec(root, 0)

        for i, _ in enumerate(levels):
            if i % 2:
                levels[i] = levels[i][::-1]

        for i, level in enumerate(levels[:-1]):
            for j, node in enumerate(level):
                if node:
                    left = j * 2
                    right = left + 1
                    node.left = levels[i+1][left]
                    node.right = levels[i+1][right]

        return root
