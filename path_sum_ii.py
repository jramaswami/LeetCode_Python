"""
LeetCode :: August 2021 Challenge :: Path Sum II
jramaswami
"""


class Solution:
    def pathSum(self, root, target_sum):


        def is_leaf(node):
            return node.left is None and node.right is None


        def traverse(node, curr_sum, curr_path, soln, target_sum):
            if node is None:
                return

            curr_sum += node.val
            curr_path.append(node.val)

            if is_leaf(node) and target_sum == curr_sum:
                soln.append(list(curr_path))

            traverse(node.left, curr_sum, curr_path, soln, target_sum)
            traverse(node.right, curr_sum, curr_path, soln, target_sum)

            curr_path.pop()


        soln = []
        traverse(root, 0, [], soln, target_sum)
        return soln
