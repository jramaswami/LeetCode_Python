"""
LeetCode
889. Construct Binary Tree from Preorder and Postorder Traversal
February 2025 Challenge
jramaswami

Thank You NeetCode.IO
"""



class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder_indexes = {x: i for i, x in enumerate(postorder)}

        def rec(preorder_left, preorder_right, postorder_left, postorder_right):
            if preorder_left > preorder_right or postorder_left > postorder_right:
                return None

            root = TreeNode(preorder[preorder_left])
            if preorder_left != preorder_right:
                left_val = preorder[preorder_left + 1]
                mid = postorder_indexes[left_val]
                left_size = mid - postorder_left + 1
                root.left = rec(preorder_left + 1, preorder_left + left_size, postorder_left, mid)
                root.right = rec(preorder_left + left_size + 1, preorder_right, mid + 1, postorder_right - 1)
            return root

        return rec(0, len(preorder)-1, 0, len(postorder)-1)
