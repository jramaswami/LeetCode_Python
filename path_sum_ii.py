"""
LeetCode :: August 2021 Challenge :: Path Sum II
jramaswami
"""


class Solution:
    def pathSum(self, root, target_sum):

        def is_leaf(node):
            """Return True if node is leaf node."""
            return node.left is None and node.right is None

        def traverse(node, curr_sum, curr_path, soln, target_sum):
            if node is None:
                return

            # Add val and node to path.
            curr_sum += node.val
            curr_path.append(node.val)

            # If the node is a leaf node and the curr_sum == target_sum
            # then we have found a root to leaf path with the right sum.
            if is_leaf(node) and curr_sum == target_sum:
                soln.append(list(curr_path))

            # If the node is not a leaf node and we have not exceeded the
            # target sum, then continue searching the path.
            if not is_leaf(node) and curr_sum < target_sum:
                traverse(node.left, curr_sum, curr_path, soln, target_sum)
                traverse(node.right, curr_sum, curr_path, soln, target_sum)

            # Remove the node from the path for later recursion.
            curr_path.pop()

        soln = []
        traverse(root, 0, [], soln, target_sum)
        return soln



#
# Testing
#
from leetcode_bst import *


def test_4():
    """WA"""
    root = make_tree([-2,null,-3])
    target = -5
    expected = [[-2,-3]]
    assert Solution().pathSum(root, target) == expected
