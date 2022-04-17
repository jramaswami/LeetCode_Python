"""
LeetCode :: April 2022 Challenge :: 897. Increasing Order Search Tree
jramaswami
"""


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def inorder(node, curr):
            if node is None:
                return curr

            curr = inorder(node.left, curr)
            curr.right = TreeNode(node.val)
            curr = curr.right
            curr = inorder(node.right, curr)
            return curr

        dummy = TreeNode(-1)
        inorder(root, dummy)
        return dummy.right
