"""
LeetCode :: 297. Serialize and Deserialize Binary Tree
jramaswami

REF: https://medium.com/coding-memo/leetcode-serialize-and-deserialize-binary-tree-c51af92e65ad
"""


import collections


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        NULL = 1024
        H = []
        # Preorder traversal.
        def preorder(node):
            if node is None:
                H.append(NULL)
            else:
                H.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return ",".join(str(i) for i in H)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        NULL = 1024
        if data == []:
            return None

        q = collections.deque(int(i) for i in data.split(','))

        def traverse():
            v = q.popleft()
            if v == NULL:
                return None
            else:
                return TreeNode(v, traverse(), traverse())

        return traverse()