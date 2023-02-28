"""
LeetCode
652. Find Duplicate Subtrees
February 2023 Challenge
jramaswami
"""


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        subtrees = dict()

        def rec(node):
            if node is None:
                return None

            key = (node.val, rec(node.left), rec(node.right))
            if key in subtrees:
                subtrees[key] = (node, subtrees[key][1] + 1)
            else:
                subtrees[key] = (node, 1)
            return key

        rec(root)
        return [node for node, freq in subtrees.values() if freq > 1]