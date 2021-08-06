"""
LeetCode :: August 2021 Challenge :: N-ary Tree Level Order Traversal
jramaswami

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root):
        soln = []
        if root:
            queue = [root]
            new_queue = []
            while queue:
                # Copy current level to solution.
                soln.append([node.val for node in queue if node is not None])
                # BFS next level.
                for node in queue:
                    for child in node.children:
                        new_queue.append(child)
                queue, new_queue = new_queue, []
        return soln
