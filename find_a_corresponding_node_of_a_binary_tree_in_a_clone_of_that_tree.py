"""
LeetCode :: May 2022 Challenge :: 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
jramaswami
"""


class Solution:

    def getTargetCopy(self, original, cloned, target):

        def traverse(onode, cnode, target):
            if onode == None:
                return

            if onode == target:
                return cnode

            result = traverse(onode.left, cnode.left, target)
            if result:
                return result

            result = traverse(onode.right, cnode.right, target)
            if result:
                return result

        return traverse(original, cloned, target)
