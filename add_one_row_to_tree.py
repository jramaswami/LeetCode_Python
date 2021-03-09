"""
LeetCode :: March 2021 Challenge :: Add One Row To Tree
jramaswami
"""
def solve0(node, node_level, target_value, target_level):
    """Recursive solution to the problem."""
    if node is None:
        return None

    if node_level == target_level - 1:
        left_node = node.left
        right_node = node.right

        new_left_node = TreeNode(target_value, left_node, None)
        new_right_node = TreeNode(target_value, None, right_node)

        return TreeNode(node.val, new_left_node, new_right_node)

    return TreeNode(node.val, solve0(node.left, node_level + 1, target_value, target_level),
                              solve0(node.right, node_level + 1, target_value, target_level))


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # Base case, insert at root.
        if d == 1:
            return TreeNode(v, root, None)
        return solve0(root, 1, v, d)

