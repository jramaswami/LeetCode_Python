"""
LeetCode
501. Find Mode in Binary Search Tree
November 2023 Challenge
jramaswami
"""


import collections


class Solution:
    def findMode(self, root):

        def rec(node):
            if node is None:
                return
            yield node.val
            yield from rec(node.left)
            yield from rec(node.right)

        freqs = collections.Counter(rec(root))
        mode_freq = max(freqs.values())
        return [k for k, v in freqs.items() if v == mode_freq]