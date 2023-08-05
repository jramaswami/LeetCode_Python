"""
LeetCode
95. Unique Binary Search Trees II
August 2023 Challenge
jramaswami
"""


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def rec(values):
            # Base case: no values:
            if len(values) == 0:
                return [None]
            # Base Case: single value left.
            if len(values) == 1:
                return [TreeNode(values[0])]

            result = []
            for v in values:
                left = [t for t in values if t < v]
                right = [t for t in values if v < t]
                left_subtrees = rec(left)
                right_subtrees = rec(right)
                for lst in left_subtrees:
                    for rst in right_subtrees:
                        root = TreeNode(v)
                        root.left = lst
                        root.right = rst
                        result.append(root)
            return result

        return rec(list(range(1, n+1)))