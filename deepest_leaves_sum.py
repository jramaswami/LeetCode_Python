"""
LeetCode :: April 2021 Challenge :: Deepest Leaves Sum
jramaswami
"""
from leetcode_trees import *


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        def dfs(node, level, max_level, level_sum):
            """DFS to find sum of deepest level nodes."""
            if node is None:
                return max_level, level_sum

            max_level, level_sum = dfs(node.left, level + 1, max_level, level_sum)
            max_level, level_sum = dfs(node.right, level + 1, max_level, level_sum)

            if level > max_level:
                return level, node.val
            elif level == max_level:
                return max_level, level_sum + node.val
            else:
                return max_level, level_sum

        return dfs(root, 0, 0, 0)[1]


# This tree is broken(!?)
# def test_1():
#     root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
#     assert Solution().deepestLeavesSum(make_tree(root)) == 15


def test_2():
    root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
    assert Solution().deepestLeavesSum(make_tree(root)) == 19
