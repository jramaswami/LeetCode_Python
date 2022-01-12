"""
LeetCode :: January 2022 Challenge :: 701. Insert into a Binary Search Tree
jramaswami
"""


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def insert(node, val):
            if node is None:
                return TreeNode(val, None, None)

            if node.val < val:
                node.right = insert(node.right, val)
            elif node.val > val:
                node.left = insert(node.left, val)
            return node

        return insert(root, val)
