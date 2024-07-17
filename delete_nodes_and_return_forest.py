"""
LeetCode
1110. Delete Nodes And Return Forest
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
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = []

        def rec(node, parent):
            if node is None:
                return

            if parent and parent.val in to_delete and node.val not in to_delete:
                # Parent was deleted, add this node to forest
                forest.append(node)

            rec(node.left, node)
            rec(node.right, node)

            if node.left and node.left.val in to_delete:
                # Child deleted, remove it
                node.left = None
            if node.right and node.right.val in to_delete:
                # Child deleted, remove it
                node.right = None

        if root and root.val not in to_delete:
            forest.append(root)
        rec(root, None)
        return forest