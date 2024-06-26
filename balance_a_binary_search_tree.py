"""
LeetCode
1382. Balance a Binary Search Tree
June 2024 Challenge
jramaswami
"""


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def make_new_tree(arr):
            if arr:
                mid = len(arr) // 2
                return TreeNode(
                    arr[mid], 
                    make_new_tree(arr[:mid]), 
                    make_new_tree(arr[mid+1:])
                )
            else:
                return None
                
        def flatten_tree(node, acc):
            if node:
                flatten_tree(node.left, acc)
                acc.append(node.val)
                flatten_tree(node.right, acc)
        
        arr = []
        flatten_tree(root, arr)
        new_tree = make_new_tree(arr)
        return new_tree
