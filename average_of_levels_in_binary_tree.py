"""
LeetCode :: March 2021 Challenge :: Average of Levels in Binary Tree
jramaswami
"""
from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # Use BFS to get levels sums and count.
        queue = deque()
        queue.append((root, 0))
        level_sums = []
        level_count = []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(level_sums) - 1 < level:
                    level_sums.append(0)
                    level_count.append(0)
                level_sums[level] += node.val
                level_count[level] += 1
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))

        return [s / c for s, c in zip(level_sums, level_count)]
