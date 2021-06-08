"""
LeetCode :: June 2021 Challenge :: Construct Binary Tree from Preorder and Inorder Traversal
jramaswami
"""


from typing import *
from leetcode_trees import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        dummy = TreeNode(None, None, None)
        parent = dummy
        i = 0
        p = 0
        nodes = {v: TreeNode(v, None, None) for v in preorder}
        visited_preorder = set()
        visited_inorder = set()
        while p < len(preorder):
            curr = nodes[preorder[p]]
            visited_preorder.add(curr.val)
            if parent.val in visited_inorder:
                parent.right = curr
            else:
                parent.left = curr
            parent = curr

            if inorder[i] == curr.val:
                while i < len(inorder) and inorder[i] in visited_preorder:
                    visited_inorder.add(inorder[i])
                    parent = nodes[inorder[i]]
                    i += 1
            p += 1

        return dummy.left


def tree_preorder(node, acc):
    if node is None:
        return
    acc.append(node.val)
    tree_preorder(node.left, acc)
    tree_preorder(node.right, acc)

def tree_inorder(node, acc):
    if node is None:
        return
    tree_inorder(node.left, acc)
    acc.append(node.val)
    tree_inorder(node.right, acc)


def test_1():
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = Solution().buildTree(preorder, inorder)
    preorder_result = []
    tree_preorder(root, preorder_result)
    inorder_result = []
    tree_inorder(root, inorder_result)
    assert preorder == preorder_result and inorder == inorder_result


def test_2():
    preorder = [-1]
    inorder = [-1]
    expected = [-1]
    root = Solution().buildTree(preorder, inorder)
    preorder_result = []
    tree_preorder(root, preorder_result)
    inorder_result = []
    tree_inorder(root, inorder_result)
    assert preorder == preorder_result and inorder == inorder_result


def test_3():
    preorder = [3,4,5,7,6,8,9,11,10]
    inorder = [7,5,4,6,8,3,11,9,10]
    root = Solution().buildTree(preorder, inorder)
    preorder_result = []
    tree_preorder(root, preorder_result)
    inorder_result = []
    tree_inorder(root, inorder_result)
    assert preorder == preorder_result 
    assert inorder == inorder_result
