"""
LeetCode :: October 2022 Challenge :: 653. Two Sum IV - Input is a BST
jramaswami
"""


class Solution:
    def findTarget(self, root, k):

        def tree_iterator(node):
            if node is None:
                return
            yield from tree_iterator(node.left)
            yield node.val
            yield from tree_iterator(node.right)

        prevs = set()
        for a in tree_iterator(root):
            if (k - a) in prevs:
                return True
            prevs.add(a)
        return False