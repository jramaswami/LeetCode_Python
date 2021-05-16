"""
LeetCode :: May 2021 Challenge :: Binary Tree Cameras
jramaswami
"""
from math import inf
from typing import *
from leetcode_trees import *


def solve(node):
    # Leaf node
    if node.left is None and node.right is None:
        # I can be watched if I have a camera.
        watched_on = 1
        # I cannot be watched from below, so this is inf.
        watched_off = inf
        # I can be unwatched from below if I am off.
        unwatched_off = 0
        return watched_on, watched_off, unwatched_off
    elif node.right is None:
        left_watched_on, left_watched_off, left_unwatched_off = solve(node.left)
        # I can be on.
        # If I am on then I will add one to the count and be watched.
        watched_on = 1 + min(left_watched_on, left_watched_off, left_unwatched_off)
        # I can be off.
        # If I am off then I will be watched if the left child is on.
        watched_off = left_watched_on
        # If I am off and the left child is off, then I am not watched from below.
        # But this means that my left node must be watched already.
        unwatched_off = left_watched_off
        return watched_on, watched_off, unwatched_off
    elif node.left is None:
        right_watched_on, right_watched_off, right_unwatched_off = solve(node.right)
        # I can be on.
        # If I am on then I will add one to the count and be watched.
        watched_on = 1 + min(right_watched_on, right_watched_off, right_unwatched_off)
        # I can be off.
        # If I am off then I will be watched if the right child is on.
        watched_off = right_watched_on
        # If I am off and the right child is off, then I am not watched from below.
        # But this means that my right node must be watched already.
        unwatched_off = right_watched_off
        return watched_on, watched_off, unwatched_off
    else:
        # I have two children.
        left_watched_on, left_watched_off, left_unwatched_off = solve(node.left)
        right_watched_on, right_watched_off, right_unwatched_off = solve(node.right)
        watched_on = watched_off = unwatched_off = inf
        # I can be on.
        # If I am on then I am watched and can use any of the ones from below.
        watched_on = (1 + min(left_watched_on, left_watched_off, left_unwatched_off) +
                          min(right_watched_on, right_watched_off, right_unwatched_off))
        # I can be off.
        # If I am off, both children will have to be watched.
        # If I am watched then one child will have to be on.
        watched_off = inf
        # The left child could be on.  The right child must be watched.
        watched_off = min(watched_off, left_watched_on + right_watched_off)
        # The right child could be on.  The left child must be watched.
        watched_off = min(watched_off, left_watched_off + right_watched_on)
        # Both children could be on.
        watched_off = min(watched_off, left_watched_on + right_watched_on)
        # If I am unwatched, then both children are off, but must be watched.
        unwatched_off = (left_watched_off + right_watched_off)
        return watched_on, watched_off, unwatched_off


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        watched_on, watched_off, unwatched_off = solve(root)
        # root must be watched.
        return min(watched_on, watched_off)
        

def test_1():
    root = make_tree([0,0,null,0,0])
    assert Solution().minCameraCover(root) == 1


def test_2():
    root = make_tree([0,0,null,0,null,0,null,null,0])
    assert Solution().minCameraCover(root) == 2


def test_3():
    """WA"""
    root = make_tree([1,2,3,null,null,null,4])
    print(root)
    assert Solution().minCameraCover(root) == 2
