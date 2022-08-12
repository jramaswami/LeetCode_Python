"""
LeetCode :: July 2021 Challenge :: Lowest Common Ancestor of a Binary Search Tree
jramaswami
"""


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def find(node, target, path):
            path.append(node)
            if node.val == target.val:
                return
            elif target.val < node.val:
                find(node.left, target, path)
            else:
                find(node.right, target, path)

        pathp = []
        find(root, p, pathp)
        pathq = []
        find(root, q, pathq)

        while pathp[-1] != pathq[-1]:
            if len(pathp) > len(pathq):
                pathp.pop()
            elif len(pathp) < len(pathq):
                pathq.pop()
            else:
                pathp.pop()
                pathq.pop()
        return pathp[-1]
