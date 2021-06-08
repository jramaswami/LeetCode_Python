"""
LeetCode :: June 2021 Challenge :: Construct Binary Tree from Preorder and Inorder Traversal
jramaswami
"""


from typing import *
from leetcode_trees import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        p = 1
        i = 0
        print(f"{preorder=}")
        print(f"{inorder=}")
        visited_preorder = dict()
        visited_inorder = dict()
        visited_preorder[preorder[0]] = TreeNode(preorder[0], None, None)
        root = current = visited_preorder[preorder[0]]
        while p < len(preorder):
            print(f"{i=} {inorder[i]=} {p=} {preorder[p]=} {current.val=}")
            while current.val == inorder[i]:
                print(f"{current.val=} == {inorder[i]=}")
                i += 1
                print(f"advancing i to {i} {inorder[i]=}")
                if i + 1 < len(inorder) and inorder[i] in visited_preorder:
                    current = visited_preorder[inorder[i]]
                    visited_inorder[inorder[i]] = current
                    print('moving current to ', current.val)

            new_node = TreeNode(preorder[p])
            visited_preorder[new_node.val] = new_node
            print(f"{i=} {inorder[i]=} {p=} {preorder[p]=} {current.val=}")
            print(f"connecting {current.val} -> {new_node.val}")
            p += 1
            # How do I know that it is right?
            if current.val in visited_inorder:
                current.right = new_node
                current = new_node
            else:
                current.left = new_node
                current = new_node
        return root


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
    print(f"{preorder=} {preorder_result=}")
    print(f"{inorder=} {inorder_result=}")
    assert preorder == preorder_result 
    assert inorder == inorder_result
