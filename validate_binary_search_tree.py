"""
LeetCode :: Validate Binary Search Tree
jramaswami
"""


import math


class Solution:
    def isValidBST(self, root):

        def traverse(node):
            # The left subtree of a node contains only nodes with keys less
            # than the node's key.
            nmin, nmax, nvalid = node.val, node.val, True
            if node.left:
                lmin, lmax, lvalid = traverse(node.left)
                if lmax >= node.val:
                    nvalid = False
                nmin = min(nmin, lmin)
                nmax = max(nmax, lmax)

            # The right subtree of a node contains only nodes with keys
            # greater than the node's key.
            if node.right:
                rmin, rmax, rvalid = traverse(node.right)
                if rmin <= node.val:
                    nvalid = False
                nmin = min(nmin, rmin)
                nmax = max(nmax, rmax)

            return nmin, nmax, nvalid

        _, _, soln = traverse(root)
        return soln



#
# Testing
#


from leetcode_bst import *


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


def test_5():
    "WA"
    root = make_tree([32,26,47,19,null,null,56,null,27])
    assert Solution().isValidBST(root) == False
