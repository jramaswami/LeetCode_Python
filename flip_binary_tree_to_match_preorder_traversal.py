"""
LeetCode :: March 2021 Challenge :: Flip Binary Tree To Match Preorder Traversal
jramaswami
"""
from typing import *
from leetcode_trees import *


def solve0(node, voyage, path, flipped):
    """Recursive solution."""
    if node is None:
        return True

    path.append(node.val)
    if path[-1] != voyage[len(path) - 1]:
        path.pop()
        return False

    # Do not swap
    if solve0(node.left, voyage, path, flipped) and solve0(node.right, voyage, path, flipped):
        return True
    # Do swap
    else:
        flipped.append(node.val)
        return solve0(node.right, voyage, path, flipped) and solve0(node.left, voyage, path, flipped)


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        path = []
        flipped = []
        if solve0(root, voyage, path, flipped):
            return flipped
        else:
            return [-1]


def test_1():
    root = [1,2]
    voyage = [2,1]
    assert Solution().flipMatchVoyage(make_tree(root), voyage) == [-1]

def test_2():
    root = [1,2,3]
    voyage = [1,3,2]
    assert Solution().flipMatchVoyage(make_tree(root), voyage) == [1]

def test_3():
    root = [1,2,3]
    voyage = [1,2,3]
    assert Solution().flipMatchVoyage(make_tree(root), voyage) == []
