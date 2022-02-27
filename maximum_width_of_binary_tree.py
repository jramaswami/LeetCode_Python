"""
LeetCode :: 662. Maximum Width of Binary Tree
jramaswami
"""


import math


class Solution:

    def widthOfBinaryTree(self, root):
        # Boundary case:
        if root is None:
            return 0

        # BFS
        queue = []
        queue.append((0, root))
        new_queue = []
        soln = 0
        while queue:
            min_index = math.inf
            max_index = -math.inf

            for index, node in queue:
                min_index = min(index, min_index)
                max_index = max(index, max_index)
                left_index = 2 * index
                right_index = left_index + 1
                if node.left:
                    new_queue.append((left_index, node.left))
                if node.right:
                    new_queue.append((right_index, node.right))

            soln = max(soln, (max_index - min_index + 1))
            queue, new_queue = new_queue, []

        return soln
