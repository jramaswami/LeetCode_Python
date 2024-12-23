"""
LeetCode
2471. Minimum Number of Operations to Sort a Binary Tree by Level
December 2024 Challenge
jramaswami
"""


from typing import Optional


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = []

        def rec(node, level):
            if node is None:
                return

            while len(levels) <= level:
                levels.append([])

            levels[level].append(node.val)
            rec(node.left, level + 1)
            rec(node.right, level + 1)

        rec(root, 0)
        swaps = 0
        for level in levels:
            sorted_level = list(sorted(level))
            locations = {x: i for i, x in enumerate(sorted_level)}
            # Sort the level
            for i, _ in enumerate(level):
                x = level[i]
                target_location  = locations[x]
                while i != target_location:
                    # Swap x with whatever is in its target location
                    level[i], level[target_location] = level[target_location], level[i]
                    swaps += 1
                    x = level[i]
                    target_location  = locations[x]
            assert level == sorted_level
        return swaps