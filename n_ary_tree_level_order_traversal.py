"""
LeetCode :: September 2022 Challenge :: 429. N-ary Tree Level Order Traversal
jramaswami
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        soln = []

        def traverse(node, level):
            if node is None:
                return

            while len(soln) <= level:
                soln.append([])

            soln[level].append(node.val)
            for child in node.children:
                traverse(child, level+1)

        traverse(root, 0)
        return soln