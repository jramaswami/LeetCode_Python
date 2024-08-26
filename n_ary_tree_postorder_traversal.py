"""
LeetCode
590. N-ary Tree Postorder Traversal
August 2024 Challenge
jramaswami
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        soln = []

        def rec(node):
            if node is None:
                return
            for child in node.children:
                rec(child)
            soln.append(node.val)

        rec(root)
        return soln
