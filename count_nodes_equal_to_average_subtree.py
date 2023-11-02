"""
LeetCode
2265. Count Nodes Equal to Average of Subtree
November 2023
jramaswami
"""


import collections


Result = collections.namedtuple('Result', ['count', 'sum', 'avgnodes'])


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        def rec(node):
            if node is None:
                return Result(0, 0, 0)

            left_result = rec(node.left)
            right_result = rec(node.right)

            my_sum = left_result.sum + right_result.sum + node.val
            my_count = left_result.count + right_result.count + 1
            my_avg = my_sum // my_count
            my_avgnodes = left_result.avgnodes + right_result.avgnodes
            if my_avg == node.val:
                my_avgnodes += 1
            return Result(my_count, my_sum, my_avgnodes)

        return rec(root).avgnodes