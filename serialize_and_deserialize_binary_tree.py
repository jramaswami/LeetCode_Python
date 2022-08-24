"""
LeetCode :: 297. Serialize and Deserialize Binary Tree
jramaswami
"""

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        H = []
        def traverse(node, i):
            if node is None:
                return

            while len(H) <= i:
                H.append(None)

            H[i] = node.val
            traverse(node.left, i*2)
            traverse(node.right, (i*2)+1)

        traverse(root, 1)
        return str(H)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        H = [t.strip() for t in data[1:-1].split(",")]

        def traverse(i):
            if i >= len(H):
                return None
            if H[i] == "None":
                return None
            left_child = traverse(i * 2)
            right_child = traverse((i * 2) + 1)
            return TreeNode(int(H[i]), left_child, right_child)

        return traverse(1)