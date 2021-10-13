"""
LeetCode :: October 2021 Challenge :: 1008. Construct Binary Search Tree from Preorder Traversal
"""
from leetcode_bst import TreeNode


from collections import namedtuple
from math import inf


SItem = namedtuple('SItem', ['node', 'subtree_max'])


class Solution:
    def bstFromPreorder(self, preorder):
        stack = []
        root = TreeNode(preorder[0])
        stack.append(SItem(root, inf))

        for n in preorder[1:]:
            # N can only go into a subtree where it does not exceed the
            # subtree's maximum value.
            while n > stack[-1].subtree_max:
                stack.pop()

            new_node = TreeNode(n)
            if n < stack[-1].node.val:
                stack[-1].node.left = new_node
                stack.append(SItem(new_node, stack[-1].node.val))
            else:
                stack[-1].node.right = new_node
                stack.append(SItem(new_node, stack[-1].subtree_max))

        return root
