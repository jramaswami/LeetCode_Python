"""
LeetCode :: Validate Binary Search Tree
jramaswami
"""
from leetcode_bst import *
from typing import *
from math import inf


def solve0(node, less_than, more_than):
    if node is None:
        return True

    if less_than <= node.val:
        return False

    if more_than >= node.val:
        return False

    return (solve0(node.left, node.val, more_than) and
            solve0(node.right, less_than, node.val))


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Invariant in binary search tree is that for a given node,
        # it is larger than all items in its left subtree and less than
        # all the items in its right subtree.
        return solve0(root, inf, -inf)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Testing

def test_1():
    root = make_tree([2,1,3])
    assert Solution().isValidBST(root) == True

def test_2():
    root = make_tree([5,1,4,null,null,3,6])
    assert Solution().isValidBST(root) == False

def test_3():
    root = make_tree([1,1])
    assert Solution().isValidBST(root) == False

def test_4():
    root = make_tree([5,4,6,null,null,3,7])
    assert Solution().isValidBST(root) == False

