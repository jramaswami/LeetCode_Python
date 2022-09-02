"""
LeetCode :: September 2022 Challenge :: 637. Average of Levels in Binary Tree
jramaswami
"""


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        level_total = []
        level_count = []

        def traverse(node, level):
            if node is None:
                return

            while len(level_total) <= level:
                level_total.append(0)
                level_count.append(0)

            level_total[level] += node.val
            level_count[level] += 1
            traverse(node.left, level+1)
            traverse(node.right, level+1)

        traverse(root, 0)
        return [t / c for t, c in zip(level_total, level_count)]