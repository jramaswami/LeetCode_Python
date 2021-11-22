"""
LeetCode :: November 2021 Challenge :: 450. Delete Node in a BST

REF: Algorithms - Sedgweick and Wayne; pp. 406-411.
"""


class Solution:
    def deleteNode(self, root, key):

        def get_min(node):
            "Return the node with the minimum value."
            if node.left:
                return get_min(node.left)
            return node

        def delete_min(node):
            "Delete the node with the minimum value."
            if node.left is None:
                return node.right

            node.left = delete_min(node.left)
            return node

        def delete_node(node, key):
            "Delete the node containing the key value."
            if node is None:
                return None

            if key < node.val:
                node.left = delete_node(node.left, key)
            elif key > node.val:
                node.right = delete_node(node.right, key)
            else:
                if node.right is None:
                    return node.left
                if node.left is None:
                    return node.right
                node0 = node
                node = get_min(node0.right)
                node.right = delete_min(node0.right)
                node.left = node0.left
            return node

        return delete_node(root, key)