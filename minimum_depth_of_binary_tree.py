"""
LeetCode
111. Minimum Depth of Binary Tree
July 2023 Challenge
jramaswami
"""


import collections


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        soln = 10**20
        
        if root is None:
            return 0
            
        def is_leaf(node):
            return node.left is None and node.right is None

        # BFS
        queue = collections.deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if is_leaf(node):
                soln = min(soln, depth)
            else:
                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))
        return soln
