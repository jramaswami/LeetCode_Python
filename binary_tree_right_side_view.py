"""
LeetCode :: July 2022 Challenge Binary Tree Right Side View
jramaswami
"""


class Solution:
    def rightSideView(self, root):

        soln = []

        def reverse_inorder(node, level):
            if node is None:
                return

            while level >= len(soln):
                soln.append(None)
            reverse_inorder(node.right, level+1)
            if soln[level] is None:
                soln[level] = node.val
            reverse_inorder(node.left, level+1)

        reverse_inorder(root, 0)
        return soln


#
# Testing
#


from leetcode_trees import *


def test_1():
    root = make_tree([1,2,3,null,5,null,4])
    expected = [1, 3, 4]
    assert Solution().rightSideView(root) == expected


def test_2():
    root = make_tree([1,null,3])
    expected = [1,3]
    assert Solution().rightSideView(root) == expected


def test_3():
    root = None
    expected = []
    assert Solution().rightSideView(root) == expected
