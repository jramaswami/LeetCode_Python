"""
LeetCode :: June 2022 Challenge :: Binary Tree Cameras
jramaswami
"""


import math


class Solution:
    def minCameraCover(self, root):

        def solve0(node):
            if node is None:
                return math.inf, 0, math.inf

            left_camera, left_covered, left_uncovered = solve0(node.left)
            right_camera, right_covered, right_uncovered = solve0(node.right)

            # Put a camera here. I cover my children so choose any status from the children.
            camera_here = 1 + min(left_camera, left_covered, left_uncovered) + min(right_camera, right_covered, right_uncovered)
            # Do not put a camera here.
            # I will be covered if there is a camera below me.
            # Since I have no camera the right node must have a camera or be covered.
            # Since I have no camera the left node must have a camera or be covered.
            covered_here = min(
                left_camera + min(right_camera, right_covered),
                right_camera + min(left_camera, left_covered)
            )
            # I will be uncovered if there is no camera below me.
            # Since I have no camera the right node must be covered.
            # Since I have no camera the left node must covered.
            uncovered_here = left_covered + right_covered
            return camera_here, covered_here, uncovered_here

        return min(*solve0(root)[:-1])


#
# TESTING
#


from leetcode_trees import *



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
