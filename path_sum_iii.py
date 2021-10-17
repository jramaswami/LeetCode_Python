"""
LeetCode :: October 2021 Challenge :: Path Sum III
jramaswami
"""


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def solve0(node, target, acc):
            if node is None:
                return 0

            acc0 = list(acc)
            # Acc is a prefix sum, so we can just look for any prefix that when
            # subtracted from our new sum creates the target.
            new_sum = acc0[-1] + node.val
            look_for = new_sum - target
            result = acc0.count(look_for)
            acc0.append(new_sum)
            acc0 = tuple(acc0)
            return result + solve0(node.left, target, acc0) + solve0(node.right, target, acc0)

        return solve0(root, targetSum, (0,))
