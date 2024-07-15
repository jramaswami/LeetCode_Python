"""
LeetCode
2196. Create Binary Tree From Descriptions
July 2024 Challenge
jramaswami
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        indegrees = {}
        for parent, child, is_left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
                indegrees[parent] = 0
            if child not in nodes:
                nodes[child] = TreeNode(child)
                indegrees[child] = 0

            indegrees[child] += 1

            if is_left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        root = None
        for node, indegree in indegrees.items():
            if indegree == 0:
                root = node
        return nodes[root]