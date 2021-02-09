"""
LeetCode :: Convert BST to Greater Tree
jramaswami
"""
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode(val={self.val} left={self.left}, right={self.right})"

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.val == other.val and self.right == other.right and self.left == other.left
        return False


def solve(node, acc):
    if node is None:
        return 0

    prev_val = node.val

    # Right
    sum_right = solve(node.right, acc)

    # Node
    node.val = prev_val + sum_right + acc

    # Left
    sum_left = solve(node.left, node.val)

    return sum_left + sum_right + prev_val
    
    
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        solve(root, 0)
        return root


def test_1():
    root = TreeNode(4, TreeNode(1, TreeNode(0, None, None), TreeNode(2, None, TreeNode(3, None, None))),
                       TreeNode(6, TreeNode(5, None, None), TreeNode(7, None, TreeNode(8, None, None))))
    expected = TreeNode(30, TreeNode(36, TreeNode(36, None, None), TreeNode(35, None, TreeNode(33, None, None))),
                       TreeNode(21, TreeNode(26, None, None), TreeNode(15, None, TreeNode(8, None, None))))
    result = Solution().convertBST(root)
    print(result)
    print(expected)
    assert result == expected
