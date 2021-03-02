"""
LeetCode :: Validate Binary Search Tree
jramaswami
"""
from typing import *
from leetcode_bst import *


def solve0(node):
    # Return if subtree is valid and the min and maxes from the subtree.
    if node is None:
        return (True, None, None)

    left_valid, left_min, left_max = solve0(node.left)
    right_valid, right_min, right_max = solve0(node.right)

    node_valid = left_valid and right_valid
    node_min = node.val
    node_max = node.val
    if left_max is not None:
        node_valid = node_valid and node.val > left_max
        node_min = min(node.val, left_min)
        node_max = max(node.val, left_max)
    if right_min is not None:
        node_valid = node_valid and node.val < right_min
        node_min = min(node.val, right_min)
        node_max = max(node.val, right_max)
    
    return (node_valid, node_min, node_max)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Invariant in binary search tree is that for a given node,
        # it is larger than all items in its left subtree and less than
        # all the items in its right subtree.
        return solve0(root)[0]


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

