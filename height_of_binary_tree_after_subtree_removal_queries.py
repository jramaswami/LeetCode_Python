"""
LeetCode
2458. Height of Binary Tree After Subtree Removal Queries
October 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        heights = collections.defaultdict(int)
        
        def get_all_heights(node):
            if node is None:
                return 0
            
            x = get_all_heights(node.left)
            y = get_all_heights(node.right)
            heights[node.val] = 1 + max(x, y)
            return heights[node.val]

        get_all_heights(root)
        
        height_if_cut = collections.defaultdict()

        def compute_heights_if_cut(node, x, h):
            if node is None:
                return
            
            # Cut current node
            height_if_cut[node.val] = max(h, x)

            a = 0
            if node.left:
                a = h + 1 + heights[node.left.val]
            b = 0
            if node.right:
                b = h + 1 + heights[node.right.val]
            
            compute_heights_if_cut(node.left, max(x, b), h+1)
            compute_heights_if_cut(node.right, max(x, a), h+1)

        compute_heights_if_cut(root, 0, 0)
        
        return [height_if_cut[x] - 1 for x in queries]
